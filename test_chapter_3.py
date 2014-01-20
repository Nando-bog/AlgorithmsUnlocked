#encoding utf-8
import chapter_3

# ([list], list_length, item, correct answer )
LISTS_FOR_SEARCH = (
    (['Adriana', 'Carlos', 'Ines', 'Jairo', 'Luisa', 'Orlando',
      'Ricardo', 'Sandra', 'Victor'], len(['Adriana', 'Carlos',
      'Ines', 'Jairo', 'Luisa', 'Orlando', 'Ricardo', 'Sandra', 'Victor']), 'Victor', 8),
    ([1, 34, 54, 1012, 2024, 3176, 3189, 4000],
        len([1, 34, 54, 1012, 2024, 3176, 3189, 4000]), 1, 0),
    ([2, 4, 6, 8, 10], len([2, 4, 6, 8, 10]), 11, False),
    (range(10), 10, 9, 10),
    (['algun', 'en', 'de', 'la', 'lugar', 'mancha'],
        len(['algun', 'en', 'de', 'la', 'lugar', 'mancha']), 'zopenco', False),
)

#List of functions to test. They must all have the same inputs, l, n, item.
SEARCH_FUNCTIONS = [chapter_3.binary_search]


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


print(test_search(LISTS_FOR_SEARCH, SEARCH_FUNCTIONS))