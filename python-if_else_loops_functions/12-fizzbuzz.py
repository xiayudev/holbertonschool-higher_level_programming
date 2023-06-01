#!/usr/bin/python3
def fizzbuzz():
    mult3 = 0
    mult5 = 0
    for x in range(1, 101):
        mult3 = x % 3
        mult5 = x % 5
        if mult3 == 0 and mult5 == 0:
            print("FizzBuzz", end=" ")
        elif mult3 == 0:
            print("Fizz", end=" ")
        elif mult5 == 0:
            print("Buzz", end=" ")
        else:
            print(x, end=" ")
