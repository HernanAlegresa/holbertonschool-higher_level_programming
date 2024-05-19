#!/usr/bin/python3
def safe_print_list_integers(my_list=[], x=0):
    elem_to_print = 0
    for i in range(x):
        try:
            if isinstance(my_list[i], int):
                print("{:d}".format(my_list[i]), end="")
                elem_to_print += 1
        except IndexError:
            continue
    print()
    return elem_to_print
