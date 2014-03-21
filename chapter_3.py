#coding=utf-8
#My versions of procedures described in chapter 3 of Cormen, T. H. (2013).
#Algorithms Unlocked. MIT Press.
#Version 0.23


def binary_search(l, n, item):
    """ Return index of item if item is in the list l.

    Return False if item is not in least.
    l --assumed to be ordered from least to greatest.
    n --an int, representing the length of l.
    item --the item to be searched.
    Binary search described in page 30.
    """

    p = 0
    r = n - 1
    q = 1
    while p <= r:
        q = (p + r) / 2
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

    list unordered_list: list to be sorted.
    int num_items: number of items in unordered_list.
    """

    for item_index in range(num_items):
        smallest_index = item_index
        for next_item_index in range(item_index+1, num_items):
            if unordered_list[next_item_index] < \
               unordered_list[smallest_index]:
                smallest_index = next_item_index
        unordered_list[item_index], unordered_list[smallest_index] = \
            unordered_list[smallest_index], unordered_list[item_index]
    return unordered_list


def insertion_sort(unordered_list, num_items):
    """Return list in ascending order using a insertion sort algorithm.

    list unordered_list: list to be sorted.
    int num_items: number of items in unordered_list.
    """

    for i in range(1, num_items):
        key, j = unordered_list[i], i-1
        while j >= 0 and unordered_list[j] > key:
            unordered_list[j+1] = unordered_list[j]
            j -= 1
        unordered_list[j+1] = key
    return unordered_list

##TODO MERGE SORT pg. 41
##TODO QUICKSORT pg. 51
##TODO PARTITION SORT pg. 54
