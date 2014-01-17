# coding=utf-8
# My versions of search procedures described in chapter 2 of Cormen, T. H. (2013). Algorithms Unlocked. MIT Press.
# Version 1.0


#Cormen defines 3 inputs, including the length of the list. That value is implied here through the use of Python's for... in construct.
#Linear search procedure described in pg. 13.
def linear_search(l, item):
    """ Returns True if item is in the list l, False if it is not."""
    r=False
    for i in l:
        if i == item:
            r = True
    return r


#Cormen defines 3 inputs, including the length of the list. That value is implied here through the use of Python's for... in construct.
#Better linear search, described in page 14.
def better_linear_search(l, item):
    """ Returns True if item is in the list l, False if it is not.
    Improves from linear_search by not checking until the end of the
    list if the item is found.
    Linear search procedure described in pg. 13."""
    for i in l:
        if i==item:
            return True
    return False


#Cormen defines 3 inputs, including the length of the list. That value is implied here through the use of Python's for... in construct.
#Sentinel linear search in pg. 16
def sentinel_linear_search(l, item):
    """ Returns True if item is in the list l, False if it is not."""
    last=l[-1]
    l[-1]=item
    counter=0
    while l[counter] != item:
        counter+=1
    l[-1]=last
    if counter < len(l)-1 or l[-1]==item:
        return True
    else:
        return False


# Recursive factorial is described in pg. 23
def factorial(n):
    """Calculates the factorial of int(n)>0 using a recursive algorithm"""
    if n<0:
        raise ValueError("El número debe ser mayor que cero.")
    if n == 0:
        return 1
    return n * factorial(n-1)


def bad_factorial(n):
    """Will throw a maximum recursion depth error.
    Calculates the factorial of int(n)>0 using a recursive algorithm that
    does not work properly because it can never reach the stop condition."""
    if n<0:
           raise ValueError("El número debe ser mayor que cero.")
    if n == 0:
        return 1
    return (bad_factorial(n+1)/n+1)


#Cormen defines 4 inputs, including the length of the list and the index of the subarray that is passed in the recursive call. here, the length of the list is implied through the use of Python's for... in construct. The recursive call is made using list slicing syntax and the stop condition modified to an empy list.
#Recursive linear search described in pg. 24. 
def recursive_linear_search(l, item):
    """Returns True if item is in list(l) 
    """
    if len(l)==0:
        return False
    elif l[0]==item:
        return True
    else:
        return recursive_linear_search(l[1:], item)