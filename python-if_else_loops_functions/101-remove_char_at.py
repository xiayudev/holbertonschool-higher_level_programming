#!/usr/bin/python3
def remove_char_at(str, n):
    copy = ""
    if n <= len(str) - 1 and n >= 0:
        for i in range(0, len(str)):
            if str[i] == str[n]:
                continue
            copy += str[i]
        return copy
    return str
