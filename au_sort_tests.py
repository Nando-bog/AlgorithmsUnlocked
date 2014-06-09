#coding=utf=8
#Tests for au_sort.py

def test_sort(func, lists):
    """Return the original list and the new list for the user to compare
    outputs.
    TODO: Automate checking for correctness
    """
    for each_list in lists:
        list_length = len(each_list)
        print (each_list, func(each_list, list_length))
    return
