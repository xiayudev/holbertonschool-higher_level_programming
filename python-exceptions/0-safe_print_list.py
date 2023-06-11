#!/usr/bin/python3
def safe_print_list(my_list=[], x=0):
    length = 0
    for elem in my_list:
        length += 1
    try:
        for i in range(x):
            print(f"{my_list[i]}", end="")
    except IndexError:
        x = length
    finally:
        print("")
    return x
