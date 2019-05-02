# file: setdefault_defaultdict.py

"""Defaultdict can faster than a standard dict.
"""

from collections import defaultdict


def standard_dict(text):
    """Count with standard dict.
    """
    d = {}
    for key in text:
        d.setdefault(key, 0)
        d[key] += 1
    return d


def default_dict(text):
    """Count with defaultdict.
    """
    dd = defaultdict(int)
    for key in text:
        dd[key] += 1
    return dd


def standard_dict_group(data):
    """Group with standard dict.
    """
    d = {}
    for key, value in data:
        d.setdefault(key, []).append(value)
    return d


def default_dict_group(data):
    """Group with defaultdict.
    """
    dd = defaultdict(list)
    for key, value in data:
        dd[key].append(value)
    return dd
