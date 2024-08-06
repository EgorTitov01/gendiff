import json
from gendiff.tree import build_diff
from gendiff.parse_files import parse_some_files
from gendiff.stylish import stylish


def test_nested_json():
    file1 = 'text_files/nested/json/nested_file1.json'
    file2 = 'text_files/nested/json/nested_file2.json'
    result_file = 'tests/fixtures/nested_result'
    result = (open(result_file)).read()

    assert stylish(build_diff(*(parse_some_files(file1, file2))))  == result


def test_nested_yaml():
    file1 = 'text_files/nested/yaml/nested_file1.yaml'
    file2 = 'text_files/nested/yaml/nested_file2.yml'
    result_file = 'tests/fixtures/nested_result'
    result = (open(result_file)).read()

    assert stylish(build_diff(*(parse_some_files(file1, file2)))) == result


def test_plain_json():
    file1 = 'text_files/plain/json/plain_file1.json'
    file2 = 'text_files/plain/json/plain_file2.json'
    result_file = 'tests/fixtures/plain_result'
    result = (open(result_file)).read()

    assert stylish(build_diff(*(parse_some_files(file1, file2))))  == result


def test_plain_yaml():
    file1 = 'text_files/plain/yaml/plain_file1.yaml'
    file2 = 'text_files/plain/yaml/plain_file2.yml'
    result_file = 'tests/fixtures/plain_result'
    result = (open(result_file)).read()

    assert stylish(build_diff(*(parse_some_files(file1, file2))))  == result
