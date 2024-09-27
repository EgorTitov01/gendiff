from gendiff.generate import generate_diff


def test_stylish_plain():
    file1 = 'text_files/plain/json/plain_file1.json'
    file2 = 'text_files/plain/yaml/plain_file2.yml'
    result_file = 'tests/fixtures/stylish_plain_result'
    result = (open(result_file)).read()

    assert generate_diff(file1, file2, 'stylish') == result


def test_nested_json():
    file1 = 'text_files/nested/json/nested_file1.json'
    file2 = 'text_files/nested/json/nested_file2.json'
    result_file = 'tests/fixtures/nested_result'
    result = (open(result_file)).read()

    assert generate_diff(file1, file2, 'stylish') == result


def test_nested_yaml():
    file1 = 'text_files/nested/yaml/nested_file1.yaml'
    file2 = 'text_files/nested/yaml/nested_file2.yml'
    result_file = 'tests/fixtures/nested_result'
    result = (open(result_file)).read()

    assert generate_diff(file1, file2, 'stylish') == result


def test_plain():
    file1 = 'text_files/nested/json/nested_file1.json'
    file2 = 'text_files/nested/yaml/nested_file2.yml'
    result_file = 'tests/fixtures/plain_result'
    result = (open(result_file)).read()

    assert generate_diff(file1, file2, 'plain') == result
