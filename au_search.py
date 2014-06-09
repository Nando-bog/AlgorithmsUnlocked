# coding=utf-8
# My attempts at search procedures described in
# Cormen, T. H. (2013). Algorithms Unlocked. MIT Press.
# Search: Linear Search, Better Linear Search,Sentinel Linear Search,
# Binary search, Recursive binary search, Recursive linear search
# This version is not organized by chapter but topics. It includes all search
# procedures from chapters 2 and 3.
# Version 1.0


def linear_search(the_list, item):
    """Return the index of the item if it is in the list l, False if it is not.

    the_list = List to be searched
    item = Item to find

    Cormen defines 3 inputs, including the length of the list.
    That value is implied here through the use of Python's for... in construct.
    Linear search procedure described in pg. 13.
    """

    r = False
    for i in range(len(l)):
        if the_list[i] == item:
            r = i
    return r


def better_linear_search(the_list, item):
    """Return the index of the item if it is in the list l, False if it is not.

    the_list = List to be searched
    item = Item to find

    Cormen defines 3 inputs, including the length of the list.
    That value is implied here through the use of Python's for... in construct.
    Better linear search, described in page 14.
    """

    for i in range(len(the_list)):
        if the_list[i] == item:
            return i
    return False


def sentinel_linear_search(the_list, item):
    """ Return the index of the item if it is in the list l, False not.

    the_list = List to be searched
    item = Item to find

    Cormen defines 3 inputs, including the length of the list.
    That value is implied here through the use of Python's for... in construct.
    Sentinel linear search described in pg. 16
    """

    last = the_list[-1]
    the_list[-1] = item
    counter = 0
    while the_list[counter] != item:
        counter += 1
    the_list[-1] = last
    if counter < len(the_list)-1 or the_list[-1] == item:
        return counter
    else:
        return False


def recursive_linear_search(the_list, item, index=0):
    """Return index of item if item is in list, False if it is not.

    Cormen defines 4 inputs, including the length of the list and the
    index of the subarray that is passed in the recursive call.
    The recursive call is made using list slicing syntax and the stop
    condition was modified to an empy list.
    Recursive linear search described in pg. 24.
    """

    num_items = len(the_list) - 1
    if index > num_items:
        return False
    elif the_list[index] == item:
        return index
    else:
        return recursive_linear_search(the_list, item, index+1)


def binary_search(the_list, item):
    """ Return index of item if item is in the list l.

    Return False if item is not in least.
    l --assumed to be ordered from least to greatest.
    n --an int, representing the length of l.
    item --the item to be searched.
    Binary search described in page 30.
    """

    lower_bound = 0
    upper_bound = len(the_list) - 1
    midpoint = 1
    while lower_bound <= upper_bound:
        midpoint = (lower_bound + upper_bound) / 2
        if the_list[midpoint] == item:
            return midpoint
        elif the_list[midpoint] > item:
            upper_bound = midpoint - 1
        elif the_list[midpoint] < item:
            lower_bound = midpoint + 1
    return False


def recursive_binary_search(the_list, item, lower_bound, upper_bound):
    """Return index of item in list l using a recursive call.

    Return False if item is not in list.
    list the_list is assumed to be ordered from low to high.
    int p and r delineate the subarray in consideration in the current
    recursion.
    item is item to search.
    Binary search recursive described in page 31.
    """

    if upper_bound > len(the_list):
        raise ValueError("r cannot be greater than the length of the \
                         list. please try again.")
    if lower_bound > upper_bound:
        return False
    else:
        midpoint = (lower_bound + upper_bound) / 2
        if the_list[midpoint] == item:
            return midpoint
        elif the_list[midpoint] > item:
            return recursive_binary_search(the_list, item,
                                           lower_bound, midpoint - 1)
        else:
            return recursive_binary_search(the_list, item, midpoint + 1,
                                           upper_bound)
