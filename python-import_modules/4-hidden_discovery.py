#!/usr/bin/python3
if __name__ == "__main__":
    import hidden_4 as h

    names = sorted(dir(h))
    for name in names:
        if name.startswith("__"):
            continue
        print("{}".format(name))
