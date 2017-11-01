# -*- coding: utf-8 -*-

"""
It’s important to be clear about the relationship between iterables and iterators: Python
obtains iterators from iterables.
The standard interface for an iterator has two methods:
__next__
    Returns the next available item, raising StopIteration when there are no more items.
__iter__
    Returns self; this allows iterators to be used where an iterable is expected, for example, in a for loop.
"""


def iterate_over_str():
    s = "ABC"
    for char in s:
        print(char)


def emulate_for():
    s = "ABCD"
    it = iter(s)
    while True:
        try:
            print(next(it))
        except StopIteration:
            del it
            break


if __name__ == '__main__':
    emulate_for()
