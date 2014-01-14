# coding=utf-8
# Search procedures described in chapter 2 of Cormen, T. H. (2013). Algorithms Unlocked. MIT Press. 
# Linear search procedure described in pg. 13. Better linear search, described in page 14. sentinel linear search in pg. 16.


def linear_search(l, item):
    """ Returns True if item is in the list l, False if it is not."""
    r=False
    for i in l:
        if i == item:
            r = True
    return r


def better_linear_search(l, item):
    """ Returns True if item is in the list l, False if it is not."""
    for i in l:
        if i==item:
            return True
    return False


def sentinel_linear_search(l, item):
    """ Returns True if item is in the list l, False if it is not."""
    last=l[-1]
    l[-1]=item
    counter=0
    while l[counter] != item:
        counter+=1
    l[-1]=last
    if (counter < len(l)) or (l[-1]==item):
        return True
    else:
        return False
    

l=['hola', 'no', "mañana", 'Clemencia', 'GLM', 1, 10, 245, 'glm']
item='GLM'
print("Using linear search for '{0}' in {1}... {2}.".format(item, l, linear_search(l, item)))
print("Using better linear search for '{0}' in {1}... {2}.".format(item, l, better_linear_search(l, item)))
print("Using sentinel linear search for '{0}' in {1}... {2}.".format(item, l, better_linear_search(l, item)))