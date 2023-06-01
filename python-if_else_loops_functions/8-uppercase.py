#!/usr/bin/python3
def uppercase(str):
    last_i = len(str) - 1
    for i, letter in enumerate(str):
        if ord(letter) >= 97 and ord(letter) < 123:
            print("{}".format(
                chr(ord(letter) - 32) if last_i != i
                else chr(ord(letter) - 32) + "\n"),
                end="")
        else:
            print("{}".format(
                letter if last_i != i else letter + "\n"),
                end="")
