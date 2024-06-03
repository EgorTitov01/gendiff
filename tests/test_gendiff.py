from gendiff.gendiff import generate_diff
import json
import yaml


def test_json():
    file1 = 'text_files/json/file1.json'
    file2 = 'text_files/json/file2.json'
    result_file = 'tests/fixtures/result.json'
    result = json.dumps(json.load(open(result_file)), indent=4)

    assert generate_diff(file1, file2) == result

def test_yaml():
    file1 = 'text_files/yaml/file1.yaml'
    file2 = 'text_files/yaml/file2.yml'
    result_file = 'tests/fixtures/result.json'
    result = json.dumps(json.load(open(result_file)), indent=4)

    assert generate_diff(file1, file2) == result
