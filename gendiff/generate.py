from gendiff.tree import build_diff
from gendiff.parse_files import parse_some_files
from gendiff.stylish import stylish
from gendiff.plain import plain


def generate_diff(file1, file2, format='stylish'):
    if format == 'plain':
        return plain(build_diff(*(parse_some_files(
            file1, file2))))
    else:
        return stylish(build_diff(*(parse_some_files(
            file1, file2))))
