import itertools


def transform_format(object_):
    match str(object_):
        case 'None':
            return 'null'
        case 'True':
            return 'true'
        case 'False':
            return 'false'
        case ' ':
            return ''


def is_empty(object_):
    if object_:
        return ' '
    else:
        return ''


def stylish(diff, replacer=' ', spaces_count=4):

    def iter_(data, depth):
        deep_indent_size = depth + spaces_count
        current_indent = replacer * depth
        indent_no_signs = (deep_indent_size - 2) * replacer      # -2 spaces, because further we add signs and a space
        lines = []
        the_set = {None, True, False, ' '}

        for node in data['children']:

            if node['key'] in the_set:
                node['key'] = transform_format(node['key'])

            if node.get('value', '_') in the_set:
                node['value'] = transform_format(node['value'])

            if node.get('value new', '_') in the_set:
                node['value new'] = transform_format(node['value new'])

            if node.get('value old', '_') in the_set:
                node['value old'] = transform_format(node['value old'])

            match node['type']:
                case 'deleted':
                    lines.append(f"{indent_no_signs}- {node['key']}:{is_empty(node['value'])}{node['value']}")
                case 'new':
                    lines.append(f"{indent_no_signs}+ {node['key']}:{is_empty(node['value'])}{node['value']}")
                case 'unchanged':
                    lines.append(f"{indent_no_signs}  {node['key']}:{is_empty(node['value'])}{node['value']}")
                case 'changed':
                    lines.append(f"{indent_no_signs}- {node['key']}:{is_empty(node['value old'])}{node['value old']}")
                    lines.append(f"{indent_no_signs}+ {node['key']}:{is_empty(node['value new'])}{node['value new']}")
                case 'changed from parent':
                    lines.append(f"{indent_no_signs}- {node['key']}: {iter_(node, deep_indent_size)}")
                    lines.append(f"{indent_no_signs}+ {node['key']}:{is_empty(node['value new'])}{node['value new']}")
                case 'changed to parent':
                    lines.append(f"{indent_no_signs}- {node['key']}:{is_empty(node['value'])}{'value old'}")
                    lines.append(f"{indent_no_signs}+ {node['key']}: {iter_(node, deep_indent_size)}")
                case 'parent':
                    lines.append(f"{indent_no_signs}{node['symbol']} {node['key']}: {iter_(node, deep_indent_size)}")

        result = itertools.chain("{", lines, [current_indent + "}"])
        return '\n'.join(result)

    return iter_(diff, 0)
