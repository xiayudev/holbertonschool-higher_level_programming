#!/usr/bin/python3
def safe_print_list_integers(my_list=[], x=0):
    length = 0
    times = 0
    for elem in my_list:
        length += 1
    try:
        for elem in range(x):
            if not isinstance(my_list[elem], int):
                continue
            print("{:d}".format(my_list[elem]), end="")
            times += 1
    except ValueError:
        pass
    print("")
    return times
