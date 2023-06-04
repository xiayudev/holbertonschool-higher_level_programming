#!/usr/bin/python3
if __name__ == "__main__":
    from sys import argv

    sum = 0
    args = argv.copy()
    args.pop(0)
    if args:
        for item in args:
            sum = sum + int(item)
    print("{}".format(sum))
