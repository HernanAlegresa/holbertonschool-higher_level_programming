#!/usr/bin/python3
for dig1 in range(10):
    for dig2 in range(dig1 + 1, 10):
        if dig1 == dig2:
            print("{:d}{:d}, ".format(dig1, dig2), end="")
        elif dig1 == 8:
            print("{:d}{:d}".format(dig1, dig2))
        else:
            print("{:d}{:d}, ".format(dig1, dig2), end="")
