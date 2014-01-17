#encoding utf-8
import chapter_2

TEST_FACTORIAL_NUMBERS=range(1,10)


LISTS_FOR_SEARCH = (
    (['hola', 'no', 'libro', 'ojo', 'good', 'bar'], 'bar', 5),
    ([1, 34, 54, 1012, 3011203040, 43, 0, -1], 1, 0),
    ([2, 4, 6, 8, 10], 11, False),
    (range(10), 9, 10),
    (['en', 'algun', 'lugar', 'de', 'lamancha'], 'enn', False),
    #(range(10**3), 9873, True),
    #(range(10**3), '4', False),
)


SEARCH_FUNCTIONS = [chapter_2.linear_search, chapter_2.better_linear_search, chapter_2.sentinel_linear_search]
FACTORIAL_FUNCTIONS=[chapter_2.factorial]


def test_search(tup, fun):
    """Tests all search functions, fun, with the list, item and correct answer from tup. Returns a tuple containing tuples of function name, item, result.
    tup is a tuple containing a list, an item to find in said list and the expected correct output.
    fun is a list of search functions to test.
    """
    res=()
    for t in tup:
        for f in fun:
            if f(t[0], t[1]) == t[2]:
                res += (f, 'ok')
            else:
                res += (f, t[1], t[2], 'problemas')
    return res


def test_recursive_linear_search(tup, fun, i):
    pass
    
def test_factorial(numbers, functions):
    """Tests each f factorial procedure using each number in iterable(n). Returns a tuple with the function, input and input!"""
    res=()
    for func in functions:
        for number in numbers:
            res+=(func, number, func(number))
    return res


print(test_search(LISTS_FOR_SEARCH, SEARCH_FUNCTIONS))
print(test_factorial(TEST_FACTORIAL_NUMBERS, FACTORIAL_FUNCTIONS))