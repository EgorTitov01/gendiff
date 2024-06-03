import json
import yaml


def parse_file_name(file_path):
    if file_path.endswith('.json'):
        data = json.load(open(file_path))
    elif file_path.endswith(('.yml', '.yaml')):
        data = yaml.safe_load(open(file_path))

    return data
