# file: intersect_magic.py
"""
Measuring the time for searching in a list and a set including
creation time of the data structure with IPython's `%timeit`.
"""

from functools import partial
import textwrap

from searching import compare
from searching_magic import calculate_ratio, timeit_magic


def intersect_list(n):
    """Measure the run time for intersecting two lists.
    """
    setup = 'list_a = range(n);list_b = range(n-3, 2 * n)'
    statement = textwrap.dedent("""
    in_both = []
    for a in list_a:
        if a in list_b:
            in_both.append(a)
    """)
    return timeit_magic(n, setup, statement)


def intersect_set(n):
    """Measure the run time for intersecting two sets.
    """
    setup = 'set_a = set(range(n));set_b = set(range(n-3, 2 * n))'
    statement = 'set_a.intersection(set_b)'
    return timeit_magic(n, setup, statement)


def main():
    """Run a timing.
    """
    func = partial(calculate_ratio, search_list=intersect_list,
                   search_set=intersect_set)
    compare(func=func, header='Intersection magic')


if __name__ == '__main__':
    main()
