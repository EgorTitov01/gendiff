

def process_nodes(data1, data2):
    nodes = []
    keys = sorted(list(data1.keys() | data2.keys()))

    for key in keys:

        if key not in data2:
            nodes.append({
                'type': 'deleted',
                'key': key,
                'value': data1[key]
            })

        elif key not in data1:
            nodes.append({
                'type': 'new',
                'key': key,
                'value': data2[key]
            })
        elif (isinstance(data1.get(key), dict)
              and isinstance(data2.get(key), dict)):
            nodes.append({
                'type': 'parent',
                'key': key,
                'children': process_nodes(data1[key], data2[key])
            })
        elif data1[key] == data2[key]:
            nodes.append({
                'type': 'unchanged',
                'key': key,
                'value': data2[key]
            })
        else:
            nodes.append({
                'type': 'changed',
                'key': key,
                'value old': data1[key],
                'value new': data2[key]
            })
    return nodes


def build_diff(data1, data2):

    return {
        'type': 'root',
        'children': process_nodes(data1, data2)
    }
