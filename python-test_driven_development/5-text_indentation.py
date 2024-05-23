#!/usr/bin/python3
"""
This module function prints a text with 2 new lines
after each of these characters: ., ? and :
"""


def text_indentation(text):
    """
    Prints a text with 2 new lines after each occurrence of '.', '?' and ':'.

    Args:
        text (str): The text to be processed.

    Raises:
        TypeError: If text is not a string.

    Returns:
        None
    """
    if not isinstance(text, str):
        raise TypeError("text must be a string")
    result = ""
    for char in text:
        result += char
        if char in [".", "?", ":"]:
            result += "\n\n"
    print(result)
