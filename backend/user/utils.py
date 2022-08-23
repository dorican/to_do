import json


def load_from_json(filename):
    with open(filename, 'r', encoding='utf-8') as file:
        return json.load(file)