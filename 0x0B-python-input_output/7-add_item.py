#!/usr/bin/python3


import sys
import json

save_to_json_file = __import__('5-save_to_json_file').save_to_json_file
load_from_json_file = __import__('6-load_from_json_file').load_from_json_file


alist = list(sys.argv[1:])

try:
    info = load_from_json_file('add_item.json')
except (TypeError, FileNotFoundError):
    info = []

info.extend(alist)
save_to_json_file(info, 'add_item.json')
