import json
import yaml


def parse_file_name(file_path1, file_path2):
    if file_path1.endswith('.json'):
        data1 = json.load(open(file_path1))
    elif file_path1.endswith(('.yml', '.yaml')):
        data1 = yaml.safe_load(open(file_path1))

    if file_path2.endswith('.json'):
        data2 = json.load(open(file_path2))
    elif file_path2.endswith(('.yml', '.yaml')):
        data2 = yaml.safe_load(open(file_path2))

    return data1, data2
