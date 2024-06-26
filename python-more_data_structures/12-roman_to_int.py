#!/usr/bin/python3
def roman_to_int(roman_string):
    roman_dic = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
    if not isinstance(roman_string, str) or roman_string is None:
        return 0
    roman_num = 0
    for i in roman_string:
        if i in roman_dic:
            roman_num += roman_dic[i]
    return roman_num
