import itertools


def transform_value(value):
    if isinstance(value, bool):
        return str(value).lower()
    elif value is None:
        return 'null'
    elif isinstance(value, dict):
        return '[complex value]'
    elif not value and value != 0:
        return "''"
    return f"'{value}'"


def plain(data, path_key='', path=''):
    if path_key:
        path = path + path_key + "."

    lines = []
    for node in data['children']:
        helpful_path = "'" + path + node['key'] + "'"
        match node['type']:
            case 'deleted':
                new_path = helpful_path
                lines.append(f"Property {new_path} "
                             f"was removed")
            case 'new':
                new_path = helpful_path
                lines.append(f"Property {new_path} "
                             f"was added with value: "
                             f"{transform_value(node['value'])}")
            case 'parent':
                lines.append(plain(node, node['key'], path))
            case 'changed':
                new_path = helpful_path
                lines.append(f"Property {new_path} "
                             f"was updated. "
                             f"From {transform_value(node['value old'])} to "
                             f"{transform_value(node['value new'])}")

    result = itertools.chain(lines)
    return '\n'.join(result)
