from gendiff.gendiff import generate_diff
import json


def test_not_empty():
    file1 = 'json_files/file1.json'
    file2 = 'json_files/file2.json'
    result_file = 'tests/fixtures/result.json'
    result = json.dumps(json.load(open(result_file)), indent=4)

    assert generate_diff(file1, file2) == result
