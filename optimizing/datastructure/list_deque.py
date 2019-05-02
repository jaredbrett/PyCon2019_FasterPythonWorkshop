# file: list_deque.py

"""Removing elements from a list vs. from a deque.
"""

from collections import deque
from statistics import mean
import timeit


def time_function(func, make_args, repeat=7, limit=1):
    """Measure the run time of a function."""
    timing_res = []
    for _ in range(repeat):
        count = 0
        duration = 0
        while duration < limit:
            args = make_args()
            start = timeit.default_timer()
            func(*args)
            duration += timeit.default_timer() - start
            count += 1
        timing_res.append(duration / count)
    return mean(timing_res)


def remove_from_list(my_list, start, end):
    """Remove elements between `start` and `end` from a list.
    """
    my_list[start:end] = []


def remove_from_deque(my_deque, start, end):
    """Remove elements between `start` and `end` from a deque.
    """
    my_deque.rotate(-end)
    for _ in range(end - start):
        my_deque.pop()
    my_deque.rotate(start)


def main():
    """Run some tests.
    """
    start = 100
    size = int(1e6)
    fmt = '{diff:10,d} {list_time:10.2e} {deque_time: 10.2e} {ratio:8.2f}'
    for limit in [0.00001, 0.0001, 0.001, 0.01, 0.1]:
        print('Limit:', limit)
        print('{:>10s} {:>10s} {:>10s} {:>8s}'.format(
            'Replaced', 'List', 'Deque', 'Ratio'))
        for end in [101, 110, 1100, 10100, 100100]:
            diff = end - start
            results = {}
            for obj, func in zip([list, deque], [remove_from_list,
                                                 remove_from_deque]):
                def make_args(obj=obj, size=size, start=start, end=end):
                    """Dynamically create function with right arguments.
                    """
                    return obj(range(size)), start, end

                res = time_function(func, make_args, limit=limit)
                results[obj.__name__] = res
            list_time = results['list']
            deque_time = results['deque']
            ratio = list_time / deque_time
            print(fmt.format(diff=diff, list_time=list_time,
                             deque_time=deque_time, ratio=ratio))


if __name__ == '__main__':
    main()
