# coding=utf-8
# My versions of procedures described in chapter 3 of Cormen, T. H.
#(2013). Algorithms Unlocked. MIT Press.
# Version 0.1

#Binary search described in page 30
def binary_search(l, n, item):
    """ Returns index of item if item is in the list l, False if it is
    not. l is assumed to be ordered from least to greatest. n is an
    int, representing the length of l"""
    p=0
    r=n-1
    q=1
    while p<=r:
        q=(p+r)/2
        if l[q]==item:
            return q
        elif l[q]>item:
            r=q-1
        elif l[q]<item:
            p=q+1
    return False
