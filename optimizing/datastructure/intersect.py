# file: intersect.py
"""
Measuring the time for searching in a list and a set including
creation time of the data structure.
"""

import timeit

from searching import compare


def intersect_list(n):
    """Measure the run time for intersecting two lists.
    """
    list_a = range(n)
    list_b = range(n-3, 2 * n)
    start = timeit.default_timer()
    in_both = []
    for x in list_a:
        if x in list_b:
            in_both.append(x)
    run_time = timeit.default_timer() - start
    return run_time, in_both


def intersect_set(n):
    """Measure the run time for intersecting two setss.
    """
    set_a = set(range(n))
    set_b = set(range(n-3, 2 * n))
    start = timeit.default_timer()
    in_both = set_a.intersection(set_b)
    run_time = timeit.default_timer() - start
    return run_time, in_both


def calculate_intersect(n):
    """Calculate the intersecting time for two lists and two sets.
    """
    list_time, list_result = intersect_list(n)
    set_time, set_result = intersect_set(n)
    assert set_result == set(list_result)
    return list_time, set_time, list_time / set_time


if __name__ == '__main__':

    compare(func=calculate_intersect, header='Intersection')
