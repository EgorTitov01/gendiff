#!usr/bin/env python3

from gendiff.cli import parse_args
from gendiff.tree import build_diff
from gendiff.parse_files import parse_some_files
from gendiff.stylish import stylish


def main():
    if parse_args()[2] == 'stylish':
        form = stylish

    print(
        form(
        build_diff(
        *(parse_some_files(
    (parse_args())[0], (parse_args())[1])
        )
        )
        )
    )



if __name__ == '__main__':

    main()
