#encoding utf-8
import chapter_3

# tuple ([list], list_length, item, correct answer)
LISTS_FOR_SEARCH = (
    (['Adriana', 'Carlos', 'Ines', 'Jairo', 'Luisa', 'Orlando',
     'Ricardo', 'Sandra', 'Victor'], len(['Adriana', 'Carlos',
     'Ines', 'Jairo', 'Luisa', 'Orlando', 'Ricardo', 'Sandra',
     'Victor']), 'Victor', 8),
    ([1, 34, 54, 1012, 2024, 3176, 3189, 4000],
        len([1, 34, 54, 1012, 2024, 3176, 3189, 4000]), 1, 0),
    ([2, 4, 6, 8, 10], len([2, 4, 6, 8, 10]), 11, False),
    (range(10), 10, 9, 9),
    (['algun', 'en', 'de', 'la', 'lugar', 'mancha'],
        len(['algun', 'en', 'de', 'la', 'lugar', 'mancha']), 'zopenco', False),
)

#List of functions to test. They must all have the same inputs, l, n, item.
SEARCH_FUNCTIONS = [chapter_3.binary_search]
SEARCH_FUNCTIONS_2 = [chapter_3.recursive_binary_search]
LISTS_FOR_SORT = (
    (['Adriana', 'Carlos', 'Ines', 'Jairo', 'Luisa', 'Orlando',
      'Ricardo', 'Sandra', 'Victor'], len(['Adriana', 'Carlos',
      'Ines', 'Jairo', 'Luisa', 'Orlando', 'Ricardo', 'Sandra', 'Victor']), ['Adriana', 'Carlos', 'Ines', 'Jairo', 'Luisa', 'Orlando', 'Ricardo', 'Sandra', 'Victor']),
    ([1, 34, 54, 1012, 2024, 3176, 3189, 4000],
        len([1, 34, 54, 1012, 2024, 3176, 3189, 4000]), [1, 34, 54, 1012, 2024, 3176, 3189, 4000]),
    ([10, 8, 6, 4, 2], len([10, 8, 6, 4, 2]), [2, 4, 6, 8, 10]),
    (['algun', 'en', 'de', 'la', 'lugar', 'mancha'],
        len(['algun', 'en', 'de', 'la', 'lugar', 'mancha']),['algun', 'de', 'en', 'la', 'lugar', 'mancha']),
)
SORT_FUNCTIONS = [chapter_3.selection_sort, chapter_3.insertion_sort]


def test_search(lists, fun):
    """Tests all search functions, fun, with the list, item and correct
    answer from tup. Returns a tuple containing tuples of function name,
    item, result.
    tup is a tuple containing a list, an item to find in said list and
    the expected correct output. fun is a list of search functions to
    test."""
    res=()
    for t in lists:
        for f in fun:
            ans=f(t[0], t[1], t[2])
            if ans==t[3]:
                res+=(f, 'ok')
            else:
                res+=(f, 'problemas con {0}'.format(t[2]))
    return res

def test_search_2(lists, fun):
    """Tests all search functions, fun, with the list, item and correct
    answer from tup. Returns a tuple containing tuples of function name,
    item, result.
    tup is a tuple containing a list, an item to find in said list and
    the expected correct output. fun is a list of search functions to
    test."""
    
    res=()
    for t in lists:
        for f in fun:
            ans = f(t[0], 0, t[1]-1, t[2])
            if ans == t[3]:
                res += (f, 'ok')
            else:
                res += (f, 'problemas con {0}'.format(t[2]))
    return res


def test_sort(lists, fun):
    """Test all sort functions, fun, with the list, item and correct
    answer.
    
    fun is an iterable of functions
    lists = ((list, list_length, correct answer), )
    
    """
    
    res=()
    for t in lists:
        for f in fun:
            ans = f(t[0], t[1])
            if ans == t[2]:
                res += (f, 'ok')
            else:
                res += (f, 'problemas con {0}'.format(t[2]))
    return res 


print(test_search(LISTS_FOR_SEARCH, SEARCH_FUNCTIONS))
print(test_search_2(LISTS_FOR_SEARCH, SEARCH_FUNCTIONS_2))
print(test_sort(LISTS_FOR_SORT, SORT_FUNCTIONS))
