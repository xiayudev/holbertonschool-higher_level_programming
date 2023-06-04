#!/usr/bin/python3
if __name__ == "__main__":
    from sys import argv

    args = "arguments"
    if len(argv) > 1:
        if len(argv) == 2:
            args = "argument"
        print("{} {}:".format(len(argv) - 1, args))
        for index, item in enumerate(argv):
            if index == 0:
                continue
            print("{}: {}".format(index, item))
    else:
        print("0 arguments.")
