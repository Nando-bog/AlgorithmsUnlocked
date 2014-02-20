#coding=utf-8
# My versions of procedures described in chapter 3 of Cormen, T. H.
#(2013). Algorithms Unlocked. MIT Press.
# Version 0.21


def binary_search(l, n, item):

    """ Return index of item if item is in the list l.

    Return False if item is not in least.
    l is assumed to be ordered from least to greatest.
    n is an int, representing the length of l.
    item is the item to be searched.
    Binary search described in page 30.
    """

    p = 0
    r = n - 1
    q = 1
    while p <= r:
        q = (p + r)/2
        if l[q] == item:
            return q
        elif l[q] > item:
            r = q - 1
        elif l[q] < item:
            p = q + 1
    return False


def recursive_binary_search(l, p, r, item):
    """Return index of item in list l using a recursive call.

    Return False if item is not in list.
    list l is assumed to be ordered from low to high.
    int p and r delineate the subarray in consideration in the current
    recursion.
    item is item to search.
    Binary search recursive described in page 31.
    """

    if r > len(l):
        raise ValueError("r cannot be greater than the length of the \
                         list. please try again.")
    if p > r:
        return False
    else:
        q = (p + r) / 2
        if l[q] == item:
            return q
        elif l[q] > item:
            return recursive_binary_search(l, p, q - 1, item)
        else:
            return recursive_binary_search(l, q + 1, r, item)


#Merge sort as described...
