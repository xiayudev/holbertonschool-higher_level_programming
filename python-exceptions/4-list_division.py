#!/usr/bin/python3
def list_division(my_list_1, my_list_2, list_length):
    result = None
    new = list()
    try:
        for i in range(list_length):
            num1 = my_list_1[i]
            num2 = my_list_2[i]
            if num2 == 0:
                new.append(0)
                print("division by 0")
                continue
            elif not isinstance(num1, int) or not isinstance(num2, int):
                new.append(0)
                print("wrong type")
                continue
            result = num1 / num2
            new.append(result)
    except IndexError:
        new.append(0)
        print("out of range")
    finally:
        pass
    return new
