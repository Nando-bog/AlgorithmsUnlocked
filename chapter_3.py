#coding=utf-8
#My attempts at procedures described in chapter 3 of Cormen, T. H. (2013).
#Search: Binary search, Recursive binary search
#Sort: Selection sort, Insertion Sort
#Algorithms Unlocked. MIT Press.
#Version 0.31


def binary_search(the_list, num_items, item):
    """ Return index of item if item is in the list l.

    Return False if item is not in least.
    l --assumed to be ordered from least to greatest.
    n --an int, representing the length of l.
    item --the item to be searched.
    Binary search described in page 30.
    """

    lower_bound = 0
    upper_bound = num_items - 1
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


def recursive_binary_search(the_list, lower_bound, upper_bound, item):
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
            return recursive_binary_search(the_list, lower_bound, midpoint - 1, item)
        else:
            return recursive_binary_search(the_list, midpoint + 1, upper_bound, item)


def selection_sort(the_list, num_items):
    """Return list in ascending order using a selection sort algorithm.

    the_list: list to be sorted.
    num_items: number of items in unordered_list.
    Selection sort described in pg. 
    """

    for item_index in range(num_items):
        smallest_index = item_index
        for next_item_index in range(item_index+1, num_items):
            if the_list[next_item_index] < \
               the_list[smallest_index]:
                smallest_index = next_item_index
        the_list[item_index], the_list[smallest_index] = \
            the_list[smallest_index], the_list[item_index]
    return the_list


def insertion_sort(the_list, num_items):
    """Return list in ascending order using a insertion sort algorithm.

    the_list: list to be sorted.
    int num_items: number of items in the_list.
    Insertion sort described in pg. 
    """

    for i in range(1, num_items):
        key, j = the_list[i], i-1
        while j >= 0 and the_list[j] > key:
            the_list[j+1] = the_list[j]
            j -= 1
        the_list[j+1] = key
    return the_list


def merge_sort(the_list):
    """Return a sorted copy of the_list
    
    the_list: list to be sorted.
    """
    
    ordered_list = []
    return ordered_list

##TODO MERGE SORT pg. 41
##TODO QUICKSORT pg. 51
##TODO PARTITION SORT pg. 54
