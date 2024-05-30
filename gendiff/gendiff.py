import json


def generate_diff(file_path1, file_path2):
    data1 = json.load(open(file_path1))
    data2 = json.load(open(file_path2))
    diff = dict()
    sorted_data1 = dict(sorted(data1.items()))

    for key_file1 in sorted_data1:

        if key_file1 not in data2:
            diff[f'- {key_file1}'] = sorted_data1[key_file1]

        elif sorted_data1[key_file1] == data2[key_file1]:
            diff[key_file1] = sorted_data1[key_file1]

        else:
            diff[f'- {key_file1}'] = sorted_data1[key_file1]
            diff[f'+ {key_file1}'] = data2[key_file1]

    for key_file2 in data2:
        if key_file2 not in sorted_data1:
            diff[f'{key_file2}'] = data2[key_file2]

    return json.dumps(diff, indent=4)
