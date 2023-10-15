import json
import os


def read(path: str):

    main_dir = os.path.dirname(os.path.abspath(__file__))

    json_path = os.path.join(main_dir, path)
    print(json_path)

    with open(json_path, 'r') as f:
        data = f.read()
        obj = json.loads(data)
        return obj


def write(obj: dict, path: str):

    main_dir = os.path.dirname(os.path.abspath(__file__))

    json_path = os.path.join(main_dir, path)

    with open(json_path, 'w') as f:
        data = json.dumps(obj)
        f.write(data)


def display(obj: dict):
    listed = ''
    for x in obj:
        if not x == 'stopper':
            listed = listed + f'{x}: {obj[x]}\n'
    listed = listed + f'Stopper: {obj["stopper"]}'
    return listed
