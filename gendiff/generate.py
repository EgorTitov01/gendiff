from gendiff.tree import build_diff
from gendiff.parse_files import parse_some_files
from gendiff.formatters.stylish import stylish
from gendiff.formatters.plain import plain
from gendiff.formatters.json import json_formatter


def generate_diff(file1, file2, format='stylish'):
    if format == 'plain':
        return plain(build_diff(*(parse_some_files(
            file1, file2))))
    elif format == 'json':
        return json_formatter(build_diff(*(parse_some_files(
            file1, file2))))
    else:
        return stylish(build_diff(*(parse_some_files(
            file1, file2))))
