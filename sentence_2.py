# -*- coding: utf-8 -*-

"""
classic iterator pattern
标准的迭代器接口有两个方法。
__next__
    返回下一个可用的元素，如果没有元素了，抛出StopIteration异常。
__iter__
    返回self，以便在应该使用可迭代对象的地方使用迭代器，例如在for循环中。

可迭代的对象有个 __iter__ 方法，每次都实例化一个新的迭代器；而迭代器要实现 __next__ 方
法，返回单个元素，此外还要实现 __iter__ 方法，返回迭代器本身。
因此，迭代器可以迭代，但是可迭代的对象不是迭代器。
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

    # 可迭代的对象有个 __iter__ 方法，每次都实例化一个新的迭代器
    def __iter__(self):
        return SentenceIterator(self.words)


class SentenceIterator(object):

    def __init__(self, words):
        self.words = words
        self.index = 0

    # The Iterator ABC abstract method is it.__next__() in Python 3 and it.next() in Python 2.
    # Here is Python, so the method's name must be next()
    def next(self):
        try:
            word = self.words[self.index]
        except IndexError:
            raise StopIteration()

        self.index = self.index + 1
        return word

    # Python 中的迭代器还实现了__iter__方法，因此迭代器也可以迭代。
    # 注意，对这个示例来说，其实没必要在 SentenceIterator 类中实现 __iter__ 方法，
    # 不过这么做是对的，因为迭代器应该实现 __next__ 和 __iter__ 两个方法，而且这么做
    # 能让迭代器通过 issubclass(SentenceInterator, abc.Iterator) 测试。
    # 如果让SentenceIterator 类继承 abc.Iterator 类，那么它会继承 abc.Iterator.__iter__
    # 这个具体方法。
    def __iter__(self):
        return self


def test_whether_iterable():
    s = Sentence("My name is xxx.")
    print(s)

    # Python语言内部会处理for循环和其他迭代上下文（如列表推导、元组拆包，等等）中的StopIteration异常。
    # 注意：此处的s是一个可迭代对象，而不是一个迭代器
    # for循环时，python调用了Sentence的__iter__方法，获取到了一个迭代器
    # 然后反复在这个迭代器上调用next函数获取下一个元素，直到迭代器抛出StopIteration异常
    # 最后python内部捕获了该异常，结束了迭代
    for word in s: # 对一个可迭代对象进行迭代
        print(word)

    # 在这边，就需要SentenceIterator当中定义了__iter__方法
    # 否则会报异常TypeError: 'SentenceIterator' object is not iterable
    for word in iter(s): # 对一个迭代器进行迭代
        print(word)

    # it = iter(s) # 从可迭代的对象中获取迭代器
    # while True:
    #     try:
    #         print(next(it)) # 在迭代器上调用next函数获取下一个元素
    #     except StopIteration: # 没有元素了迭代器会抛出StopIteration异常
    #         del it # 释放对 it 的引用，即废弃迭代器对象
    #         break

    print(list(s))

    # error, because Sentence has no __getitem__ method.
    # print(s[100000])

    # error, because Sentence has no __len__ method.
    # print(len(s))


if __name__ == '__main__':
    test_whether_iterable()
