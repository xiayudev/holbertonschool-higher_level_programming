#!/usr/bin/python3
def search_replace(my_list, search, replace):
    new = [replace if search == num else num for num in my_list]
    return new
