# -*- coding: utf-8 -*-

"""
# Why Sequences Are Iterable: The iter Function
# Whenever the interpreter needs to iterate over an object x, it automatically calls iter(x).
# The iter built-in function:
#   1. Checks whether the object implements __iter__, and calls that to obtain an iterator.
#   2. If __iter__ is not implemented, but __getitem__ is implemented, Python creates
#   an iterator that attempts to fetch items in order, starting from index 0 (zero).
#   3. If that fails, Python raises TypeError, usually saying “C object is not iterable,” where
#   C is the class of the target object.

# I guess the sequence protocol include:
#   1. __getitem__
#   2. __len__
"""

import re
import reprlib

WORDS_PAT = re.compile(r'\w+')


class Sentence(object):

    def __init__(self, text):
        self.text = text
        self.words = WORDS_PAT.findall(text)

    def __getitem__(self, index):
        return self.words[index]

    def __len__(self):
        return len(self.words)

    def __repr__(self):
        return "Sentence(%s)" % reprlib.repr(self.text)


def main():
    text = Sentence("Those, who have committed copyright violations, will be prosecuted accordingly.")

    # it is iterable
    for item in text:
        print(item)

    # because it defines a __repr__ method
    print(text)

    # it is iterable
    print(list(text))

    # it is a sequence, so we can get words by index
    print(text[0])
    print(len(text))

    # Sequences are all iterable
    # Why?
    # That is why any Python sequence is iterable: they all implement __getitem__.



if __name__ == '__main__':
    main()
