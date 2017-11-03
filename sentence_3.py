# -*- coding: utf-8 -*-

"""
Now the iterator in Example 14-5 is in fact a generator object, built automatically when the __iter__ method is called,
because __iter__ here is a generator function.

How a Generator Function Works
Any Python function that has the yield keyword in its body is a generator function:
a function which, when called, returns a generator object. In other words, a generator
function is a generator factory.

A generator function builds a generator object that wraps the body of the function.
When we invoke next(…) on the generator object, execution advances to the next yield
in the function body, and the next(…) call evaluates to the value yielded when the func‐
tion body is suspended. Finally, when the function body returns, the enclosing generator
object raises StopIteration, in accordance with the Iterator protocol.
"""

import re
import reprlib

WORDS_PAT = re.compile(r'\w+')
# Generators are iterators that produce the values of the expressions passed to yield.


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

    print(list(s))


if __name__ == '__main__':
    main()