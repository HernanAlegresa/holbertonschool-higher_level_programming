#!/usr/bin/env python3
"""
1. Pickling Custom Classes
"""
import json


class CustomObject:
    def __init__(self, name, age, is_student):
        self.name = name
        self.age = age
        self.is_student = student


    def display(self):
        print(f"Name: {name}")
        print(f"Age: {age}")
        print(f"Is Student: {is_student}")


    def serialize_and_save_to_file(self, filename):
        with open(filename, "w") as file:
            pickle.dump(self, file)


    @classmethod
    def deserialize(cls, filename):
        try:
            with open(filename, "r") as file:
                filename = pickle.load(file)
                return filename
        except (FileNotFoundError, #malformedfiles):
            return None