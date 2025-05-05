from gendiff.generate import generate_diff
from config import PROJECT_ROOT_str


def test_stylish_plain():
    file1 = PROJECT_ROOT_str + '/tests/text_files/plain/json/plain_file1.json'
    file2 = PROJECT_ROOT_str + '/tests/text_files/plain/yaml/plain_file2.yml'
    result_file = PROJECT_ROOT_str + '/tests/fixtures/stylish_plain_result'
    result = (open(result_file)).read()

    assert generate_diff(file1, file2, 'stylish') == result


def test_nested_json():
    file1 = PROJECT_ROOT_str + '/tests/text_files/nested/json/nested_file1.json'
    file2 = PROJECT_ROOT_str + '/tests/text_files/nested/json/nested_file2.json'
    result_file = PROJECT_ROOT_str + '/tests/fixtures/nested_result'
    result = (open(result_file)).read()

    assert generate_diff(file1, file2, 'stylish') == result


def test_nested_yaml():
    file1 = PROJECT_ROOT_str + '/tests/text_files/nested/yaml/nested_file1.yaml'
    file2 = PROJECT_ROOT_str + '/tests/text_files/nested/yaml/nested_file2.yml'
    result_file = PROJECT_ROOT_str + '/tests/fixtures/nested_result'
    result = (open(result_file)).read()

    assert generate_diff(file1, file2, 'stylish') == result


def test_plain():
    file1 = PROJECT_ROOT_str + '/tests/text_files/nested/json/nested_file1.json'
    file2 = PROJECT_ROOT_str + '/tests/text_files/nested/yaml/nested_file2.yml'
    result_file = PROJECT_ROOT_str + '/tests/fixtures/plain_result'
    result = (open(result_file)).read()

    assert generate_diff(file1, file2, 'plain') == result
