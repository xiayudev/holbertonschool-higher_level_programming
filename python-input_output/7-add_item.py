#!/usr/bin/python3
"""Module to work with JSON"""


# Imports to work with
import json
from sys import argv
from os.path import exists
load_from_json_file = __import__('6-load_from_json_file').load_from_json_file
save_to_json_file = __import__('5-save_to_json_file').save_to_json_file

FILENAME = "add_item.json"
args = argv[1:]  # Take just arguments not filename
file_exists = exists(FILENAME)  # Check if file exists

if file_exists:
    to_obj = load_from_json_file(FILENAME)  # Save the previous object
    with open(FILENAME, mode="w", encoding="utf-8") as f:
        to_obj = to_obj + args
        save_to_json_file(to_obj, FILENAME)
else:
    with open(FILENAME, mode="w", encoding="utf-8") as f:
        save_to_json_file(args, FILENAME)
