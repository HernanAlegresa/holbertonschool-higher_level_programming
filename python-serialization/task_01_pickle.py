#!/usr/bin/env python3
"""
1. Pickling Custom Classes
"""
import json


class CustomObject:
    def __init__(self, name, age, is_student):
        self.name = name
        self.age = age
        self.is_student = is_student

    def display(self):
        print(f"Name: {self.name}")
        print(f"Age: {self.age}")
        print(f"Is Student: {self.is_student}")

    def serialize(self, filename):
        with open(filename, "w") as file:
            pickle.dump(self, file)

    @classmethod
    def deserialize(cls, filename):
        try:
            with open(filename, "r") as file:
                filename = pickle.load(file)
                return filename
        except (FileNotFoundError, pickle.UnpicklingError):
            return None
