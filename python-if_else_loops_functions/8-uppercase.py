#!/usr/bin/python3
def uppercase(str):
    last_index = len(str) - 1
    last_chr = ""
    for i, letter in enumerate(str):
        if (i == last_index):
            last_chr = "\n"
        if ord(letter) >= 97 and ord(letter) < 123:
            print("{}".format(chr(ord(letter) - 32)), end=last_chr)
        else:
            print("{}".format(letter), end=last_chr)
