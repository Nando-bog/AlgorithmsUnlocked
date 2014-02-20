#coding=utf-8
#My versions of procedures described in chapter 3 of Cormen, T. H. (2013).
#Algorithms Unlocked. MIT Press.
#Version 0.22


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


def selection_sort(unordered_list, num_items):
    """Return list in ascending order using a selection sort algorithm.

    list unurdered list: list to be sorted.
    int items number of items in l.

    Selection sort described in page 33. Not implemented exactly as Cormen's.
    The final step does not swap the i-th and smallest elements in the list,
    but moves the smallest to the position of the i-th element and all others
    to the next one by using the insert method of Python lists.
    """

    for item_index in range(num_items):
        smallest_index = item_index
        for next_item_index in range(item_index, num_items):
            if unordered_list[next_item_index] < unordered_list[item_index]:
                smallest_index = next_item_index
        ##Pop smallest and insert before item_index instead of swap smallest
        ##with item_index
        unordered_list.insert(item_index, unordered_list.pop(smallest_index))
    return unordered_list


##TODO SELECTION SORT pg. 32
##TODO INSERTION SORT pg. 35
##TODO MERGE SORT pg. 41
##TODO QUICKSORT pg. 51
##TODO PARTITION SORT pg. 54