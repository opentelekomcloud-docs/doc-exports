#!/usr/bin/env python3

import argparse
import bs4
import json
import os
import pathlib
import re
import subprocess
import warnings


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


def get_target_path(code, metadata, path=''):
    if code in metadata:
        current = metadata[code]
        if not current.get('p_code'):
            return current['new_name']
        else:
            return (
                "{0}/{1}".format(
                    get_target_path(current['p_code'], metadata),
                    current['new_name'])
            )
    else:
        return ''


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


def flatten_html(soup):
    for i in soup.body.find_all('div'):
        if "note" in i.get('class', []):
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
            del i['id']
            if i.img:
                i.img.decompose()
            i['class'] = 'important'
        elif "caution" in i.get('class', []):
            del i['id']
            if i.img:
                i.img.decompose()
        elif "fignone" in i.get('class', []):
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
        else:
            i.name = 'p'
    for tbl in soup.body.find_all('table'):
        tbl_id = tbl.get('id')
        if tbl_id:
            tbl['id'] = re.sub('[-_]', '', tbl_id)

    return soup.body


def main():
    parser = argparse.ArgumentParser(description='Process links.')
    parser.add_argument(
            'path', type=str, help='path to the files')
    args = parser.parse_args()
    retval = os.getcwd()
    os.chdir(args.path)
    meta_data = json.loads(open("CLASS.TXT.json").read())
    metadata_by_uri = dict()
    metadata_by_code = dict()
    rename_matrix = dict()
    table_re = re.compile(r'.*<table[^>]+ id="([^"]+)"')
    for f in meta_data:
        f['new_name'] = get_new_name(f['title'])
        metadata_by_uri[f['uri']] = f
        metadata_by_code[f.get('code')] = f

    tree = build_doc_tree(metadata_by_code)

    for f in meta_data:
        # Construct link renaming matrix
        target_path = get_target_path(f['p_code'], metadata_by_code)
        if target_path:
            target_path += '/'
        name = f["new_name"] if not tree.get(f['code']) else f"{f['new_name']}/index"
        rename_matrix[f['uri']] = f"{target_path}{name}.html"

    pathlib.Path("temp/").mkdir(parents=True, exist_ok=True)
    docs_anchors = dict()

    for f in pathlib.Path().glob("*.html"):
        if f.name not in metadata_by_uri:
            continue
        # Registering section links
        with open(f, 'r') as reader:
            print(f"scanning {f.name}")
            content = reader.read()
            soup = bs4.BeautifulSoup(content, "lxml")
            for lnk in soup.body.find_all('div', class_='section'):
                title = lnk.find('h4')
                anchor = None
                if title.string:
                    anchor = title.string
                elif title.strings:
                    anchor = ''.join(title.strings)
                if anchor:
                    title = re.sub('[ _:]', '-', anchor)
                    res = dict(
                        fname=f.name,
                        title=title,
                        replace=title.lower()
                    )
                    docs_anchors[lnk.get('id')] = res

    for f in pathlib.Path().glob("*.html"):
        if f.name not in metadata_by_uri:
            continue
        _target = metadata_by_uri[f.name]
        target = _target['new_name']
        target_path = get_target_path(_target['p_code'], metadata_by_code)
        target_deepness = target_path.count('/') + 1
        if not _target['p_code']:
            # we only +1 if we are not on the same level
            target_deepness = 0
        pathlib.Path("temp/").mkdir(parents=True, exist_ok=True)
        pathlib.Path("tmp_result/" + target_path).mkdir(
                parents=True, exist_ok=True)
        pathlib.Path("result/" + target_path).mkdir(
                parents=True, exist_ok=True)

        # Pre-processing of html content
        with open(f, 'r') as reader, open(f"temp/{target}.tmp", 'w') as writer:
            print(f"Processing {target}")
            doc_anchors = dict()
            content = reader.read()
            soup = bs4.BeautifulSoup(content, "lxml")
            proc = flatten_html(soup)
            # Fix cross links
            for lnk in proc.find_all("a"):
                href = lnk.get('href')
                if href:
                    page_url = ''
                    anchor = ''
                    href_parts = href.split('#')
                    if href_parts[0] in rename_matrix:
                        page_url = ('../' * target_deepness) + \
                            rename_matrix[href_parts[0]]
                    else:
                        page_url = href_parts[0]
                    if len(href_parts) > 1:
                        anchor = href_parts[1]
                        if anchor in docs_anchors:
                            anchor = docs_anchors[anchor]['replace']
                        else:
                            anchor = re.sub('[-_]', '', anchor).lower()
                        lnk['href'] = f"{page_url}#{anchor}"
                    else:
                        lnk['href'] = lnk['href'].replace(
                                href_parts[0],
                                page_url)
                if not href:
                    lnk_name = lnk.get('name')
                    if (
                            lnk_name and not lnk.string
                            and lnk_name not in doc_anchors
                    ):
                        lnk['id'] = lnk_name
                        doc_anchors[lnk_name] = 1

            for line in str(proc).splitlines():
                table_match = table_re.match(line)
                if table_match:
                    writer.write(f".. _{table_match.group(1)}:\n\n")
                if not line.startswith("<strong>Parent topic:</strong>"):
                    processed_line = line
                    writer.write(processed_line + '\n')
        # Convert html to rst
        os.system(
            f"pandoc 'temp/{target}.tmp' -f html "
            f"-o 'tmp_result/{target_path}/{target}.rst' "
            f"--ascii -s --wrap none"
        )
        # Post processing of rendered rst
        with (
            open(f"tmp_result/{target_path}/{target}.rst", 'r') as reader,
            open(f"result/{target_path}/{target}.rst", 'w') as writer
        ):
            print(f"Post processing {target}")
            for line in reader.readlines():
                processed_line = re.sub(r'\.\. \\_', '\n\n.. _', line)
                processed_line = re.sub(r'√', 'Y', processed_line)
                processed_line = re.sub(
                    r'public_sys-resources/', '', processed_line)
                processed_line = re.sub(
                    r'image:: ', 'image:: /_static/images/', processed_line)
                processed_line = re.sub(
                    r'   :name: .*$', '', processed_line)
                processed_line = re.sub(
                    r'\*\*Parent topic:.*$', '', processed_line)
                processed_line = re.sub(
                    r'.. code:: screen$',
                    r'.. code-block::', processed_line)
                # spaces are important, since code-block may be inside of the
                # cell
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
        if k != 0:
            curr = metadata_by_code[k]
            title = curr['title']
            path = get_target_path(curr['code'], metadata_by_code)
        with open(f"result/{path}/index.rst", "w") as index:
            index.write('='*(len(title)) + '\n')
            index.write(title + '\n')
            index.write('='*(len(title)) + '\n')
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
            print(f"{p.resolve()} is removed in favour"
                  f" of result/{path}/index.rst")
            p.unlink()

    os.chdir(retval)


if __name__ == "__main__":
    main()
