#!/usr/bin/python3
def uppercase(str):
    for i, letter in enumerate(str):
        if ord(letter) >= 97 and ord(letter) < 123:
            letter = chr(ord(letter) - 32)
        print("{}".format(letter), end="")
    print("")
