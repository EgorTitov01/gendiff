#!usr/bin/env python3

from gendiff.cli import parse_args
from gendiff.stylish import stylish
from gendiff.generate import generate_diff


def main():
    if parse_args()[2] == 'stylish':
        format = stylish
        print(generate_diff(parse_args()[0], parse_args()[1], format))


if __name__ == '__main__':

    main()
