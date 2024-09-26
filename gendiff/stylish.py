import itertools


replacer = ' '
spaces_count = 4


def transform_format(object_, depth):
    if isinstance(object_, bool):
        return str(object_).lower()
    elif object_ is None:
        return 'null'
    elif isinstance(object_, dict):
        lines = []
        deep_indent_size = depth + spaces_count
        deep_indent = replacer * deep_indent_size
        current_indent = replacer * depth
        for key in object_:
            lines.append(f"{deep_indent}"
                         f"{key}: "
                         f"{transform_format(object_[key], deep_indent_size)}")
        result = itertools.chain("{", lines, [current_indent + "}"])
        return '\n'.join(result)
    else:
        return object_


def is_empty(object_):
    if object_:
        return ' '
    else:
        return ''


def stylish(data, depth=0):
    deep_indent_size = depth + spaces_count
    current_indent = replacer * depth
    indent_no_signs = (deep_indent_size - 2) * replacer
    lines = []

    for node in data['children']:
        if 'value' in node:
            value = transform_format(node.get('value'),
                                     deep_indent_size)
        if 'value new' in node:
            value_new = transform_format(node.get('value new'),
                                         deep_indent_size)
            value_old = transform_format(node.get('value old'),
                                         deep_indent_size)

        match node['type']:
            case 'deleted':
                lines.append(f"{indent_no_signs}- {node['key']}:"
                             f"{is_empty(value)}{value}")
            case 'new':
                lines.append(f"{indent_no_signs}+ {node['key']}:"
                             f"{is_empty(value)}{value}")
            case 'parent':
                lines.append(f"{indent_no_signs}"
                             f"  "
                             f"{node['key']}: "
                             f"{stylish(node, deep_indent_size)}")
            case 'unchanged':
                lines.append(f"{indent_no_signs}  {node['key']}:"
                             f"{is_empty(value)}{value}")
            case 'changed':
                lines.append(f"{indent_no_signs}- {node['key']}:"
                             f"{is_empty(value_old)}"
                             f"{value_old}")

                lines.append(f"{indent_no_signs}+ "
                             f"{node['key']}:"
                             f"{is_empty(value_new)}"
                             f"{value_new}")

    result = itertools.chain("{", lines, [current_indent + "}"])
    return '\n'.join(result)
