# file: searching_creation.py

"""
Measuring the time for searching in a list and a set including
creation time of the data structure.
"""

from functools import partial
import textwrap

from searching import compare
from searching_magic import calculate_ratio, timeit_magic


def search_set(n):
    """Search for an element in a set.
    """
    setup = 'my_list = list(range(n))'
    statement = textwrap.dedent("""
    my_set = set(my_list)
    n in my_set
    """)
    return timeit_magic(n, setup, statement)


def main():
    """Run some timings.
    """
    func = partial(calculate_ratio, search_set=search_set)
    compare(func=func, header='Measure creation')


if __name__ == '__main__':
    main()
