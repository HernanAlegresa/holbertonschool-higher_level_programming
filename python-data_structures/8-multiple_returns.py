#!/usr/bin/python3
def multiple_returns(sentence):
    length = len(sentence)
    for char in range(length):
        if length <= 0:
            return (0, None)
        else:
            first_char = sentence[0]
        return (length, first_char)
