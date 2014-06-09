# coding=utf-8
# My attempts at search procedures described in
# Cormen, T. H. (2013). Algorithms Unlocked. MIT Press.
# Sort algorithms: Selection sort, Insertion sort, Merge sort, Quick sort
# Version 1.0

MERGE_CALLS = 0

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


def merge_sort(the_list, p, r):
    """Return a sorted the_list

    the_list: list to be sorted.
    p, r: starting and ending indices of a subarray of the_list
    
    I HAVE NOT BEEN ABLE TO USE PYTHON TO CREATE THE ALGORITHM THAT CORMEN DESCRIBES
    I BELIEVE 0-INDEXED LISTS AND THE USE OF INFINITY ARE THE PROBLEM.
    I WILL MOST LIKELY QUIT ATTEMPTING AND CREATE MY OWN VERSION, HOPEFULLY
    MORE PYTHONICLY THAN WHAT CORMEN DESCRIBES.
    """
    pass

#print(merge_sort([3, 1,], 0, 1))
#print(merge_sort([1,5,4], 0, 2))
#print(merge_sort([1,3,2,4], 0, 3))
#print(merge_sort(["Helena", "Clemencia", "Orlando", "Leopoldo", "Nando", "Juanita"], 0, 5))
#print(merge_sort([1, 3, 5, 2, 4, 6], 0, 5))
#print(merge_sort([5, 7, 1, 0, 9], 0, 4))
#print("Merge sort was called {0} times.".format(MERGE_CALLS))
#print(merge_sort([1], 0, 0))
##TODO MERGE SORT pg. 41
##TODO QUICKSORT pg. 51
##TODO PARTITION SORT pg. 54
