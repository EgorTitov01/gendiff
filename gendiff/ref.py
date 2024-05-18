import argparse


def show_reference():
    parser = argparse.ArgumentParser(
        description='Compares two configuration files and '
                    'shows a difference.',
        usage='gendiff [-h] first_file second_file')
    parser.add_argument('first_file')
    parser.add_argument('second_file')
    parser.add_argument('-f', '--format', help='set format of output')
    args = parser.parse_args()
