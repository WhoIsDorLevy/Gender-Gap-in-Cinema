import json
import os

def read_jsonfile_to_dic(name):
    with open(os.path.join("resources", name), 'r') as file:
        return json.load(file)