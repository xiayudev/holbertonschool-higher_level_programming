#!/usr/bin/python3
if __name__ == "__main__":
    import calculator_1 as calc
    a = 10
    b = 5
    symbol = ["+", "-", "*", "/"]
    funcs = [calc.add, calc.sub, calc.mul, calc.div]
    for i, func in enumerate(funcs):
        print("{0} {3} {1} = {2}".format(a, b, func(a, b), symbol[i]))
