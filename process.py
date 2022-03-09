#!/usr/bin/env python3

import json
import os
import pathlib
import re
import warnings

def get_new_name(current_name):
    new_name = current_name.replace(' - ','_')
    new_name = new_name.replace(' ','_')
    new_name = new_name.replace('/','_')
    new_name = new_name.replace('\'','')
    new_name = new_name.replace('\"','')
    new_name = new_name.replace('\`','')
    new_name = new_name.replace('\´','')
    new_name = new_name.replace(':','')
    new_name = new_name.replace('?','')
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
    tree = dict()
    flat_tree = dict()
    for k, v in metadata.items():
        parent_id = v.get('p_code')
        if not parent_id:
            parent_id = 0

        if parent_id not in flat_tree:
            flat_tree[parent_id] = list()
        flat_tree[parent_id].append(v)
    return flat_tree


def main():
    meta_data = json.loads(open("CLASS.TXT.json").read())
    metadata_by_uri = dict()
    metadata_by_code = dict()
    table_re = re.compile(r'.*<table[^>]+ id="([^"]+)"')
    for f in meta_data:
        f['new_name'] = get_new_name(f['title'])
        metadata_by_uri[f['uri']] = f
        metadata_by_code[f.get('code')] = f

    tree = build_doc_tree(metadata_by_code)

    for f in pathlib.Path().glob("*.html"):
        if not f.name in metadata_by_uri:
            continue
        _target = metadata_by_uri[f.name]
        target = _target['new_name']
        target_path = get_target_path(_target['p_code'], metadata_by_code)
        pathlib.Path("temp/").mkdir(parents=True, exist_ok=True)
        pathlib.Path("tmp_result/" + target_path).mkdir(parents=True, exist_ok=True)
        pathlib.Path("result/" + target_path).mkdir(parents=True, exist_ok=True)

        # Pre-processing of html content
        with open(f, 'r') as reader, open(f"temp/{target}.tmp", 'w') as writer:
            print(f"Processing {target}")
            for line in reader.readlines():
                table_match = table_re.match(line)
                if table_match:
                    writer.write(f".. _{table_match.group(1)}:\n\n")
                if not line.startswith("<strong>Parent topic:</strong>"):
                    # Drop all divs
                    processed_line = re.sub(r'<[/]?div[^>]*>', '', line)
                    writer.write(processed_line)
        # Convert html to rst
        os.system(
            f"pandoc 'temp/{target}.tmp' -f html "
            f"-o 'tmp_result/{target_path}/{target}.rst' "
            f"--column 120 --ascii -s --wrap preserve"
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
                processed_line = re.sub(r'public_sys-resources/', '', processed_line)
                processed_line = re.sub(r'image:: ', 'image:: /_static/images/', processed_line)
                processed_line = re.sub(r'   :name: .*$', '', processed_line)
                processed_line = re.sub(r'**Parent topic:.*$', '', processed_line)
                processed_line = re.sub(r'.. code:: screen', '.. code-block::', processed_line)
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
            index.write('   :maxdepth:1\n\n')
            for child in v:
                new_name = child['new_name']
                if child['code'] in tree:
                    # If this is folder - add /index
                    new_name = new_name + '/index'
                index.write(f"   {new_name}\n")


        p = pathlib.Path(f"result/{path}.rst")
        if p.exists():
            print(f"{p.resolve()} is removed in favour"
                  f"of result/{path}/index.rst")
            p.unlink()


if __name__ == "__main__":
    main()
