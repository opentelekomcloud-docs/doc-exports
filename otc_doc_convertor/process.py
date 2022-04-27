#!/usr/bin/env python3

import argparse
import bs4
import json
import logging
import os
import pathlib
import re


class OTCDocConvertor:

    def __init__(self):
        self.doc_anchors = dict()
        self.doc_links = dict()

    @staticmethod
    def get_new_name(current_name):
        new_name = current_name.replace(' - ', '_')
        new_name = new_name.replace(' ', '_')
        new_name = new_name.replace('/', '_')
        new_name = new_name.replace('\'', '')
        new_name = new_name.replace('"', '')
        new_name = new_name.replace('`', '')
        new_name = new_name.replace('´', '')
        new_name = new_name.replace(':', '')
        new_name = new_name.replace('?', '')
        new_name = new_name.replace('(', '')
        new_name = new_name.replace(')', '')
        new_name = new_name.lower()
        return new_name

    @staticmethod
    def build_doc_tree(metadata):
        flat_tree = dict()
        for k, v in metadata.items():
            parent_id = v.get('p_code')
            if not parent_id:
                parent_id = 0

            if parent_id not in flat_tree:
                flat_tree[parent_id] = list()
            flat_tree[parent_id].append(v)
        return flat_tree

    @classmethod
    def get_target_path(cls, code, metadata, path=''):
        if code in metadata:
            current = metadata[code]
            if not current.get('p_code'):
                return current['new_name']
            else:
                return (
                    "{0}/{1}".format(
                        cls.get_target_path(current['p_code'], metadata),
                        current['new_name'])
                )
        else:
            return ''

    def make_label(self, soup, name):
        label = soup.new_tag("p")
        label.string = f"..\\_{name.lower()}:"
        return label

    def is_element_referred(self, ref, fname):
        return (
            ref in self.doc_links
            or '#' + ref in self.doc_links
            or fname + '#' + ref in self.doc_links
        )

    def streamline_html(self, soup, file_name):
        # Drop eventual header duplicated anchors
        fname = file_name.replace(".html", "").lower()
        met_page_anchors = dict()
        for lnk in soup.body.find_all("a"):
            name = None
            if "name" in lnk.attrs and lnk.string is None:
                name = lnk.attrs["name"].lower()
                if name in met_page_anchors:
                    # Such anchor already existed on this page, drop it
                    lnk.decompose()
                met_page_anchors[name] = True

            if name and name.lower() == fname:
                lnk.decompose()

        # Process divs
        for i in soup.body.find_all('div'):
            if "note" in i.get('class', []):
                # Notes
                del i['id']
                if i.img:
                    i.img.decompose()
                notetitle = i.find('span', class_='notetitle')
                if notetitle:
                    title = soup.new_tag('div')
                    title['class'] = 'title'
                    title.string = 'Note:'
                    notetitle.replace_with(title)
            elif "notice" in i.get('class', []):
                # Notices
                del i['id']
                if i.img:
                    i.img.decompose()
                i['class'] = 'important'
            elif "caution" in i.get('class', []):
                # Cautions
                del i['id']
                if i.img:
                    i.img.decompose()
            elif "fignone" in i.get('class', []):
                # Figures
                # When we found figure generate local label (anchor)
                if i.get('id'):
                    logging.debug('place figure label')
                    i.insert_before(self.make_label(soup, i.get("id")))
                figure = soup.new_tag('figure')
                img = i.find('img')
                cap = i.find('span', class_='figcap')
                if cap is not None:
                    cap.name = 'figcaption'
                    figure.append(cap)
                if img:
                    img['src'] = '/_static/images/' + img['src']
                    figure.append(img)
                i.replace_with(figure)
            elif "section" in i.get('class', []):
                # Sections
                # When we found section generate local label (anchor)
                if i.get('id'):
                    sec_id = i.get("id").lower()
                    if self.is_element_referred(sec_id, file_name):
                        logging.debug('Add section label')
                        i.insert_before(self.make_label(soup, sec_id))
                # and still convert to paragraph
                i.name = 'p'
            else:
                i.name = 'p'

        # Drop strong in table headers "/"
        for th in soup.body.find_all('th'):
            if th.p.strong:
                th.p.strong.unwrap()

        if self.args.improve_table_headers:
            # Add spaces around "/"
            for th in soup.body.find_all('th'):
                if hasattr(th, 'p') and th.p.string:
                    th.p.string = re.sub(
                        r'\b/\b',
                        ' / ',
                        th.p.string)

        # local anchors
        for lnk in soup.body.find_all("a"):
            if (
                lnk.string is None
                and hasattr(lnk, "name")
                and not re.match(r"^li\d+$", lnk.attrs["name"])
                # anywhere section
                and not re.match(r".*section\d+$", lnk.attrs["name"])
                # starts with table
                and not re.match(r"^table\d+$", lnk.attrs["name"])
            ):
                # Verify this is really called from somewhere:
                local_ref = lnk["name"].lower()
                if self.is_element_referred(local_ref, file_name):
                    # We now know something in the document wants this anchor -
                    # replace it with label
                    lnk.name = "p"
                    lnk.string = f"..\\_{local_ref}:"
                    del lnk["name"]
                else:
                    logging.debug("Dropping unreferred link")

        for li in soup.body.find_all("li"):
            del li['id']

        for pre in soup.body.find_all("pre"):
            text = pre.get_text()
            # if text.startswith("{"):
            #    pre["class"] = "data"
            if re.search(
                r'\[[a-z]*@\w+.*\][\s#>]?',
                text
            ):
                # Something like "[root@ecs-test-0001 ~]#"
                pre["class"] = "console"
            elif re.match(
                r'^(GET|PUT|POST|DELETE)',
                text
            ):
                # Something like "DELETE https://some_url"
                pre["class"] = "text"

        # And now specialities
        rawize_strings = [
            # "\*\*\*\*\*\*",
            # r"([\\\/\:\*\?\"\~|<>]{4,})"
        ]
        for to_rawize in rawize_strings:
            for p in soup.body.find_all(string=re.compile(to_rawize)):
                if p.string:
                    curr = p.string
                    part = re.search(to_rawize, curr)
                    if len(part.groups()) > 0:
                        new = curr.replace(
                            part.group(1),
                            f"<code>{part.group(1)}</code>"
                        )
                        p.replace_with(bs4.BeautifulSoup(new, 'html.parser'))
                        print(part.group(1))
                        print(f"New content is {p.string}")
                logging.error(f"String with star: {p}")

        return soup.body

    def main(self):
        logging.basicConfig(level=logging.DEBUG)
        parser = argparse.ArgumentParser(description='Process links.')
        parser.add_argument(
            'path', type=str, help='path to the files')
        parser.add_argument(
            '--improve-table-headers', action='store_true',
            help='Improve table headers by enforcing spaces around `/`')
        parser.add_argument(
            '--pygments-lexer',
            help='Set particular code-block lexer language')
        self.args = parser.parse_args()
        retval = os.getcwd()
        os.chdir(self.args.path)
        meta_data = json.loads(open("CLASS.TXT.json").read())
        metadata_by_uri = dict()
        metadata_by_code = dict()

        for f in meta_data:
            f['new_name'] = self.get_new_name(f['title'])
            metadata_by_uri[f['uri']] = f
            metadata_by_code[f.get('code')] = f

        tree = self.build_doc_tree(metadata_by_code)

        pathlib.Path("temp/").mkdir(parents=True, exist_ok=True)

        # Scan all docs for anchors
        for f in pathlib.Path().glob("*.html"):
            if f.name not in metadata_by_uri:
                continue
            # Registering section links
            with open(f, 'r') as reader:
                logging.debug(f"Scanning {f.name}")
                content = reader.read()
                soup = bs4.BeautifulSoup(content, "lxml")
                for lnk in soup.body.find_all('a'):
                    if "name" in lnk.attrs and lnk.string is None:
                        anchor = lnk.attrs["name"]
                        title = re.sub('[ _:]', '-', anchor)
                        res = dict(
                            fname=f.name,
                            title=title,
                            replace=title.lower()
                        )
                        self.doc_anchors[anchor] = res
                    if "href" in lnk.attrs and lnk["href"]:
                        self.doc_links[lnk["href"].lower()] = f.name

        for f in pathlib.Path().glob("*.html"):
            if f.name not in metadata_by_uri:
                continue
            _target = metadata_by_uri[f.name]
            target = _target['new_name']
            target_path = self.get_target_path(
                _target['p_code'], metadata_by_code)
            pathlib.Path("temp/").mkdir(parents=True, exist_ok=True)
            pathlib.Path("tmp_result/" + target_path).mkdir(
                parents=True, exist_ok=True)
            pathlib.Path("result/" + target_path).mkdir(
                parents=True, exist_ok=True)

            # Pre-processing of html content
            with open(f, 'r') as reader, \
                 open(f"temp/{target}.tmp", 'w') as writer:
                # if f.name not in [
                #         "modelarts_21_0031.html",
                #         "en-us_topic_0032380449.html"]:
                #     continue
                logging.info(f"Pre-Processing {f} as {target}")
                content = reader.read()
                soup = bs4.BeautifulSoup(content, "lxml")
                proc = self.streamline_html(soup, f.name)

                for lnk in proc.find_all("a"):
                    href = lnk.get('href')
                    if href and not href.startswith('http'):
                        # Internal link - replace with :ref:
                        code = soup.new_tag('code')
                        code['class'] = "interpreted-text"
                        code['role'] = "ref"
                        href_parts = href.split('#')
                        if len(href_parts) > 1:
                            # for anchor just use anchor ref
                            link_target = href_parts[1].lower()
                        else:
                            # for other page - use only page name
                            link_target = href_parts[0].replace(
                                ".html", "").lower()
                        if link_target:
                            # Looks like an anchor on the same page
                            code.string = f"{lnk.string} <{link_target}>"
                            logging.debug(f" replace {lnk} with {code}")
                            lnk.replace_with(code)

                # Drop parent link at the bottom of the page
                for parent in proc.find_all("p", class_="parentlink"):
                    parent.decompose()

                logging.info(f'Saving file {writer.name}')
                writer.write(str(proc))

            # Convert html to rst
            os.system(
                f"pandoc 'temp/{target}.tmp' -f html "
                f"-o 'tmp_result/{target_path}/{target}.rst' "
                f"--ascii -s --wrap none"
            )
            # Post processing of rendered rst
            with open(f"tmp_result/{target_path}/{target}.rst", 'r') \
                 as reader, \
                 open(f"result/{target_path}/{target}.rst", 'w') as writer:
                logging.info(f"Post processing {target}")
                writer.write(f":original_name: {f.name}\n\n")
                # Add root file label
                writer.write(f".. _{f.name.replace('.html', '')}:\n\n")
                # post process some usual stuff
                for line in reader.readlines():
                    processed_line = re.sub(r'\.\.\\_', '.. _', line)
                    processed_line = re.sub(r'√', 'Y', processed_line)
                    processed_line = re.sub(
                        r'public_sys-resources/', '', processed_line)
                    processed_line = re.sub(
                        r'image:: ', 'image:: /_static/images/',
                        processed_line)
                    processed_line = re.sub(
                        r'   :name: .*$', '', processed_line)
                    processed_line = re.sub(
                        r'\*\*Parent topic:.*$', '', processed_line)
                    processed_line = re.sub(
                        r'.. code:: screen$',
                        r'.. code-block::', processed_line)
                    for lexer in ["json", "bash", "text"]:
                        processed_line = re.sub(
                            f".. code:: {lexer}$",
                            f".. code-block:: {lexer}", processed_line)
                        if re.match(rf".. code:: {lexer}\s", processed_line):
                            logging.error(
                                f"'code-block: {lexer}' with something "
                                "afterwards")
                            exit(1)
                    # spaces are important, since code-block may reside inside
                    # of the cell
                    processed_line = re.sub(
                        r'.. code:: screen\s',
                        r'.. code-block::  ', processed_line)
                    processed_line = re.sub(
                        r'.. code:: codeblock$',
                        r'.. code-block::', processed_line)
                    writer.write(processed_line)

        # Generate indexes
        for k, v in tree.items():
            path = ''
            title = 'Main Index'
            page_label = ''
            if k != 0:
                curr = metadata_by_code[k]
                title = curr['title']
                page_label = curr['uri'].replace(".html", "").lower()
                path = self.get_target_path(curr['code'], metadata_by_code)
            with open(f"result/{path}/index.rst", "w") as index:
                if page_label:
                    index.write(f".. _{page_label}:\n\n")
                index.write('=' * (len(title)) + '\n')
                index.write(title + '\n')
                index.write('=' * (len(title)) + '\n')
                index.write('\n')
                index.write('.. toctree::\n')
                index.write('   :maxdepth: 1\n\n')
                for child in v:
                    new_name = child['new_name']
                    if child['code'] in tree:
                        # If this is folder - add /index
                        new_name = new_name + '/index'
                    index.write(f"   {new_name}\n")

            p = pathlib.Path(f"result/{path}.rst")
            if p.exists():
                logging.warning(
                    f"{p.resolve()} is removed in favour"
                    f" of result/{path}/index.rst")
                p.unlink()

        os.chdir(retval)


if __name__ == "__main__":
    OTCDocConvertor().main()
