#!/usr/bin/python3
def only_diff_elements(set_1, set_2):
    """Return a list with just unique elements
    For each word in set_1, if set_2 does not contain that word, add it to
    the new list
    """
    new = [word for word in set_1 if word not in set_2]
    new.extend([word for word in set_2 if word not in set_1])
    return new
