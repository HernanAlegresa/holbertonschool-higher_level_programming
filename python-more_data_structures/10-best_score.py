#!/usr/bin/python3
def best_score(a_dictionary):
    if not a_dictionary:
        return None
    best_value = max(a_dictionary.values())
    for key in a_dictionary:
        if a_dictionary[key] == best_value:
            return key
