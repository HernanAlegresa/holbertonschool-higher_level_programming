#!/usr/bin/env python3
"""
2. Converting CSV Data to JSON Format
"""
import csv
import json


def convert_csv_to_json(csv_file):
    data = []
    try:
        with open(csv_file, 'r') as csvfile:
            dic_reader = csv.DictReader(csv_file)
            for row in dic_reader:
                data.append(row)

        with open('data.jason', 'w') as jsonfile:
            json.dump(data, jsonfile)

        return True
    except Exception:
        return False
