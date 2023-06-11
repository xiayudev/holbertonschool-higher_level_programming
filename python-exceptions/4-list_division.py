#!/usr/bin/python3
def list_division(my_list_1, my_list_2, list_length):
    result = None
    new = list()
    try:
        for i in range(len(my_list_1)):
            num1 = my_list_1[i]
            num2 = my_list_2[i]
            if my_list_2[i] == 0:
                new.append(0)
                print("division by 0")
                continue
            elif not isinstance(num1, int) or not isinstance(num2, int):
                new.append(0)
                print("wrong type")
                continue
            result = my_list_1[i] / my_list_2[i]
            new.append(result)
    except Exception:
        pass
    finally:
        new.append(0)
        print("out of range")
    return new
