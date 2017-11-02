# -*- coding: utf-8 -*-

"""
classic iterator pattern
"""

import re
import reprlib

WORDS_PAT = re.compile(r'\w+')


class Sentence(object):

    def __init__(self, text):
        self.words = WORDS_PAT.findall(text)
        self.text = text

    def __repr__(self):
        return "Sentence(%s)" % reprlib.repr(self.text)

    def __iter__(self):
        return SentenceIterator(self.words)


class SentenceIterator(object):

    def __init__(self, words):
        self.words = words
        self.index = 0

    # The Iterator ABC abstract method is it.__next__() in Python 3 and it.next() in Python 2.
    # So here, the method's name must be next()
    def next(self):
        try:
            word = self.words[self.index]
        except IndexError:
            raise StopIteration()

        self.index = self.index + 1
        return word

    def __iter__(self):
        return self


def test_whether_iterable():
    s = Sentence("My name is xxx.")
    print(s)

    for word in s:
        print(word)

    print(list(s))

    # error, because Sentence has no __getitem__ method.
    # print(s[100000])

    # error, because Sentence has no __len__ method.
    # print(len(s))


if __name__ == '__main__':
    test_whether_iterable()
