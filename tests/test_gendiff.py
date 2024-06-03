from gendiff.gendiff import generate_diff
import json


def test_not_empty():
    file1 = 'json_files/file1.json'
    file2 = 'json_files/file2.json'
    result = json.dumps({
    "- follow": False,
    "host": "hexlet.io",
    "- proxy": "123.234.53.22",
    "- timeout": 50,
    "+ timeout": 20,
    "verbose": True
}, indent=4)

    assert generate_diff(file1, file2) == result
