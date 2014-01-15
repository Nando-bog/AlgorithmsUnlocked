# coding=utf-8
# Search procedures described in chapter 2 of Cormen, T. H. (2013). Algorithms Unlocked. MIT Press. 
# Linear search procedure described in pg. 13. Better linear search, described in page 14. sentinel linear search in pg. 16.
# Recursive factorial is described in pg. 23

def run_search(tup, fun):
    """Tests all search functions, fun, with the list, item and correct answer from tup. Returns a tuple containing tuples of function name, item, result.
    tup is a tuple containing a list, an item to find in said list and the expected correct output.
    fun is a list of search functions to test.
    """
    res=()
    for t in tup:
        for f in fun:
            if f(t[0], t[1]) == t[2]:
                res += (f, t[1], 'ok')
            else:
                res += (f, t[1], 'problemas')
    return res
    

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
    if counter < len(l)-1 or l[-1]==item:
        return True
    else:
        return False


def factorial(n):
    """Calculates the factorial of int(n)>0 using a recursive algorithm"""
    if n<0:
        raise ValueError("El número debe ser mayor que cero.")
    if n == 0:
        return 1
    return n * factorial(n-1)

nfac=-1


#l=['hola', 'no', "mañana", 'Clemencia', 'GLM', 1, 10, 245, 'glm']
#item='no joda maldita sea'
#print("Using linear search for '{0}' in {1}... {2}.".format(item, l, linear_search(l, item)))
#print("Using better linear search for '{0}' in {1}... {2}.".format(item, l, better_linear_search(l, item)))
#print("Using sentinel linear search for '{0}' in {1}... {2}.".format(item, l, sentinel_linear_search(l, item)))
#print("Calculando {0}!... = {1}".format(nfac, factorial(nfac)))


tup = (
    (['hola', 'no', 'libro', 'ojo', 'good', 'bar'], 'bar', True),
    ([1, 34, 54, 1012, 3011203040, 43, 0, -1], 1, True),
    ([2, 4, 6, 8, 10], 11, False),
    (range(10), 9, True),
    (range(10**3), 9873, True),
    (range(10**3), '4', False),
)

fun = [linear_search, better_linear_search, sentinel_linear_search]

print(run_search(tup, fun))