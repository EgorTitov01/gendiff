#!usr/bin/env python3

from gendiff.cli import parse_args
from gendiff.generate import generate_diff


def main():
    format = parse_args()[2]
    print(generate_diff(parse_args()[0], parse_args()[1], format))


if __name__ == '__main__':

    main()
