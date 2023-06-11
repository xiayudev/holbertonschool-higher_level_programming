#!/usr/bin/python3
def roman_to_int(roman_string):
    if type('a') != type(roman_string) or not roman_string:
        return 0
    roman = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
    values = [roman[char] for char in roman_string]
    total = 0
    for i, val in enumerate(values):
        if i > 0:
            if values[i] == 5 and values[i - 1] == 1:
                val = 3
            elif values[i] == 10 and values[i - 1] == 1:
                val = 8
            elif values[i] == 50 and values[i - 1] == 10:
                val = 30
            elif values[i] == 100 and values[i - 1] == 10:
                val = 80
            elif values[i] == 500 and values[i - 1] == 100:
                val = 300
            elif values[i] == 1000 and values[i - 1] == 100:
                val = 800
        total += val
    return total
