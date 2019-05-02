# file: searching_magic.py
"""
Measuring the time for searching in a list and a set with IPythom %timeit.
"""

from IPython.terminal.interactiveshell import TerminalInteractiveShell

from searching import compare


def timeit_magic(n, setup, statement):
    """Create a `%timeit` magic function with fixed `n`,
    more setup code and the statement to be timed.
    """
    return TerminalInteractiveShell().run_cell_magic(
        'timeit', '-o -q n = {n}; '.format(n=n) + setup, statement)


def search_list(n):
    """
    Search for last element in a list.
    """
    setup = 'my_list = list(range(n))'
    statement = 'n in my_list'
    return timeit_magic(n, setup, statement)


def search_set(n):
    """Search for an element in a set.
    """
    setup = 'my_set = set(range(n))'
    statement = 'n in my_set'
    return timeit_magic(n, setup, statement)


def calculate_ratio(n, search_list=search_list, search_set=search_set):
    """Calculate the ratio between a search in a list and a set.
    """
    list_time = search_list(n).average
    set_time = search_set(n).average
    return list_time, set_time, list_time / set_time


if __name__ == '__main__':
    compare(func=calculate_ratio, header='Magic timeit')
