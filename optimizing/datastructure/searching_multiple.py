# file: searching_multiple.py
"""
Measuring the time for searching in a list and a set multiple times.
"""

from statistics import mean
import timeit

from searching import compare


def search_multiple(obj, n, repeat=7):
    """Search `repeat` times for at least 1 second.
    """
    res = []
    for _ in range(repeat):
        count = 0
        duration = 0
        while duration < 1:
            start = timeit.default_timer()
            n in obj  # pylint: disable=pointless-statement
            duration += timeit.default_timer() - start
            count += 1
        res.append(duration / count)
    return mean(res)


def calculate_ratio_mutiple(n):
    """Calculate the ratio between a search in a list and a set.
    """
    my_list = list(range(n))
    my_set = set(range(n))
    list_time = search_multiple(my_list, n)
    set_time = search_multiple(my_set, n)
    return list_time, set_time, list_time / set_time


if __name__ == '__main__':

    compare(func=calculate_ratio_mutiple, header='Multiple runs')
