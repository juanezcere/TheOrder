import json


def read_json(file):
    """
    Read a json file.
    """
    f = open(file)
    data = json.load(f)
    return data