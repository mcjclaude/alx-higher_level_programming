#!/usr/bin/python3
"""Add all arguments to a Python list and save them to a file. victor"""
import sys

if __name__ == "__main__":
    save_to_json_file = __import__('5-save_to_json_file').save_to_json_file
    load_from_json_file = \
        __import__('6-load_from_json_file').load_from_json_file

    try:
        items = load_from_json_file("add_item.json")
 #!/usr/bin/python3
from os import path
from sys import argv
save_to_json_file = __import__('7-save_to_json_file').save_to_json_file
load_from_json_file = __import__('8-load_from_json_file').load_from_json_file

if path.exists('add_item.json'):
    obj_json_file = load_from_json_file('add_item.json')
else:
    obj_json_file = []

for i in range(1, len(argv)):
    obj_json_file.append(argv[i])

save_to_json_file(obj_json_file, 'add_item.json')
)