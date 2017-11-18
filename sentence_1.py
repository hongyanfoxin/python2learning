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

我们要明确可迭代的对象和迭代器之间的关系： Python 从可迭代的对象中获取迭代器。
使用 iter 内置函数可以获取迭代器的对象。如果对象实现了能返回迭代器的
__iter__ 方法，那么对象就是可迭代的。序列都可以迭代；实现了 __getitem__ 方
法，而且其参数是从零开始的索引，这种对象也可以迭代。
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
