#!/usr/bin/env python3

import json
import argparse
import subprocess


def main():
    parser = argparse.ArgumentParser(description='Process links.')
    parser.add_argument(
            'path', type=str, help='path to the files')
    args = parser.parse_args()
    matrix = json.loads(open("matrix.json").read())
    for k, v in matrix.items():
        replace = v.replace('/', '\/')
        subprocess.run(
            f"find {args.path} -name *'.rst' -type f -print0 | xargs"
            f" -0 sed -i '' 's/{k}/{replace}/g'",
            shell=True
        )
        print(k, v)


if __name__ == "__main__":
    main()
