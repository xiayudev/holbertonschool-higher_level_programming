#!/usr/bin/python3
for num in range(0, 10):
    for num2 in range(num, 10):
        if num == 8 and num2 == 9:
            print("{0}{1}".format(num, num2))
            break
        if num != num2:
            print("{0}{1}".format(num, num2), end=", ")
