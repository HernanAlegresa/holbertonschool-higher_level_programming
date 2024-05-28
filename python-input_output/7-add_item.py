#!/usr/bin/python3
"""
7. Load, add, save
"""
import sys


save_to_json_file = __import__('5-save_to_json_file').save_to_json_file
load_from_json_file = __import__('6-load_from_json_file').load_from_json_file

filename = "add_item.json"

try:
    with open(filename, "r") as file:
        list_json = load_from_json_file(filename)
except FileNotFoundError:
    list_json = []

for arguments in sys.argv[:1]:
    list_json.append(arguments)

save_to_json_file(list_json, filename)
