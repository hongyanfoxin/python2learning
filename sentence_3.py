# -*- coding: utf-8 -*-

"""
Now the iterator in Example 14-5 is in fact a generator object, built automatically when the __iter__ method is called,
because __iter__ here is a generator function.

# Generators are iterators that produce the values of the expressions passed to yield.

How a Generator Function Works
Any Python function that has the yield keyword in its body is a generator function:
a function which, when called, returns a generator object. In other words, a generator
function is a generator factory.

A generator function builds a generator object that wraps the body of the function.
When we invoke next(…) on the generator object, execution advances to the next yield
in the function body, and the next(…) call evaluates to the value yielded when the func‐
tion body is suspended. Finally, when the function body returns, the enclosing generator
object raises StopIteration, in accordance with the Iterator protocol.

实现相同功能，但却符合 Python 习惯的方式是，用生成器函数代替 SentenceIterator类。
"""

import re
import reprlib

WORDS_PAT = re.compile(r'\w+')


class Sentence(object):

    def __init__(self, text):
        self.text = text
        self.words = WORDS_PAT.findall(text)

    def __repr__(self):
        return "Sentence(%s)" % reprlib.repr(self.text)

    def __iter__(self):
        for word in self.words:
            yield word
        return

        # above can be replaced by:
        # return iter(self.words)


def main():
    s = Sentence("He is a good man.")
    print(s)

    for word in s:
        print(word)

    it = iter(s) # 从可迭代的对象中获取迭代器，此处的结果是一个generator
    while True:
        try:
            print(next(it)) # 在迭代器上调用next函数获取下一个元素，generator的功能：produce the values of the expressions passed to yield
        except StopIteration: # 没有元素了迭代器会抛出StopIteration异常
            del it # 释放对 it 的引用，即废弃迭代器对象
            break

    print(list(s))


if __name__ == '__main__':
    main()