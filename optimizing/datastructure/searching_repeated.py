# file: searching_repeated.py
"""
Measuring the time for searching in a list and a set including
creation time of the data structure.
"""

from functools import partial
import textwrap

from searching import compare
from searching_magic import calculate_ratio, timeit_magic


def search_list(n, m):
    """Search for an element in a set.
    """
    setup = 'my_list = list(range(n));m = {m}'.format(m=m)
    statement = textwrap.dedent("""
    for x in range(m):
        n in my_list
    """)
    return timeit_magic(n, setup, statement)


def search_set(n, m):
    """Search for an element in a set.
    """
    setup = 'my_list = list(range(n));m = {m}'.format(m=m)
    statement = textwrap.dedent("""
    my_set = set(my_list)
    for x in range(m):
        n in my_set
    """)
    return timeit_magic(n, setup, statement)


def main():
    """Run some timings.
    """
    for m in [10, 100, 1000, 10000]:
        func = partial(calculate_ratio,
                       search_list=partial(search_list, m=m),
                       search_set=partial(search_set, m=m))
        compare(func=func, header='Measure for {} repetitions'.format(m))


if __name__ == '__main__':
    main()
