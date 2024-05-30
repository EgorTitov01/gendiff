#!usr/bin/env python3

from gendiff.cli import parse_args
from gendiff.gendiff import generate_diff


def main():
    print(generate_diff(*(parse_args())))


if __name__ == '__main__':
    main()
