# file: searching.py
"""Measuring the time for searching in a list and a set.
"""

import timeit


def search_list(n):
    """
    Search for element that is not in a list.
    """
    my_list = list(range(n))
    start = timeit.default_timer()
    n in my_list  # pylint: disable=pointless-statement
    return timeit.default_timer() - start


def search_set(n):
    """Search for an element in a set.
    """
    my_set = set(range(n))
    start = timeit.default_timer()
    n in my_set  # pylint: disable=pointless-statement
    return timeit.default_timer() - start


def calculate_ratio(n):
    """Calculate the ratio between a search in a list and a set.
    """
    list_time = search_list(n)
    set_time = search_set(n)
    return list_time, set_time, list_time / set_time


def compare(end=8, func=calculate_ratio, header='', col1='List', col2='Set'):
    """Show the results.
    """
    table_width = 43
    print()
    if header:
        print('=' * table_width)
        print(header)
        print('=' * table_width)
    width = end + end // 3
    print('{:>{width}s} {:>9s} {:>9s} {:>12s}'.format(
        'Size', col1, col2, 'Ratio', width=width))
    print('-' * table_width)
    fmt = '{count:{width},d} {list_time:9.2e} {set_time:9.2e} {ratio:12,.2f}'
    for n in range(1, end):
        count = 10 ** n
        list_time, set_time, ratio = func(count)

        print(fmt.format(count=count, ratio=ratio, list_time=list_time,
                         set_time=set_time, width=width))
    print('=' * table_width)


if __name__ == '__main__':
    compare(header='Single run')
