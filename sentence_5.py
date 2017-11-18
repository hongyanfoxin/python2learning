# -*- coding: utf-8 -*-

"""
A Generator Expression
So, a generator expression produces a generator

A generator expression can be understood as a lazy version of a list comprehension:
it does not eagerly build a list, but returns a generator that will lazily produce the items on demand.
In other words, if a list comprehension is a factory of lists, a generator
expression is a factory of generators.

So, a generator expression produces a generator.
"""

import re
import reprlib

WORDS_PAT = re.compile(r'\w+')


class Sentence(object):

    def __init__(self, text):
        self.text = text

    def __repr__(self):
        return "Sentence(%s)" % reprlib.repr(self.text)

    def __iter__(self):
        return (match.group() for match in WORDS_PAT.finditer(self.text))


def test_whether_iterable():
    s = Sentence("I am a good student. But i am stupid and simple.")

    print(s)

    for word in s:
        print(word)

    print(list(s))


if __name__ == '__main__':
    test_whether_iterable()
