# -*- coding: utf-8 -*-

"""
a lazy Sentence class
re.finditer: a lazy version of re.findall which, instead of a list,
returns a generator producing re.MatchObject instances on demand.

A generator function builds a generator object that wraps the body of the function.
When we invoke next(…) on the generator object, execution advances to the next yield
in the function body, and the next(…) call evaluates to the value yielded when the func‐
tion body is suspended. Finally, when the function body returns, the enclosing generator
object raises StopIteration, in accordance with the Iterator protocol.
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
        for match in WORDS_PAT.finditer(self.text):
            yield match.group()


def test_whether_iterable():
    s = Sentence("I am a good student.")

    print(s)

    for word in s:
        print(word)

    print(list(s))


if __name__ == '__main__':
    test_whether_iterable()
