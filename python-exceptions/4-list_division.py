#!/usr/bin/python3
def list_division(my_list_1, my_list_2, list_length):
    result = None
    new = list()
    """Catch an error
    Catch an error, if there is one, every division made with two lists.
    If we try to put the loop inside a try, once an error is caught, the
     |_ loop is finished.
    """
    for i in range(list_length):
        try:
            result = my_list_1[i] / my_list_2[i]
            new.append(result)
        except ZeroDivisionError:
            new.append(0)
            print("division by 0")
        except IndexError:
            new.append(0)
            print("out of range")
        except TypeError:
            new.append(0)
            print("wrong type")
        finally:
            pass
    return new
