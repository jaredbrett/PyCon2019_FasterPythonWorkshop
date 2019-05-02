from functools import partial
from statistics import mean
import timeit

from searching import compare
from searching_magic import calculate_ratio, timeit_magic


def use_on(iterable):
    result = []
    for item in iterable:
        result.insert(0, item)
    return result


def use_o1(iterable):
    result = []
    for item in iterable:
        result.append(item)
    result.reverse()
    return result

def use_reversed(iterable):
    return list(reversed(iterable))


def call_multiple(func, *args, repeat=7):
    """Search `repeat` times for at least 1 second.
    """
    res = []
    for _ in range(repeat):
        count = 0
        duration = 0
        while duration < 1:
            start = timeit.default_timer()
            func(*args)  # pylint: disable=pointless-statement
            duration += timeit.default_timer() - start
            count += 1
        res.append(duration / count)
    return mean(res)


def main():
    """Run some timings.
    """
    print('{:>10s} {:>8s} {:>8s} {:>7s}'.format('Size', 'insert', 'append', 'Ratio'))
    fmt = '{size:10,d} {time_on:8.2e} {time_o1:8.2e} {ratio:7.2f}'
    for exp in range(1, 7):
        iterable = list(range(10 ** exp))
        time_on = call_multiple(use_on, iterable)
        time_o1 = call_multiple(use_o1, iterable)
        print(fmt.format(size=len(iterable), time_on=time_on, time_o1=time_o1,
                         ratio=time_on/time_o1))


if __name__ == '__main__':
    main()
