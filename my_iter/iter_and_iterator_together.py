# -*- coding:utf-8 -*-
from collections import Iterable,Iterator


class MyRange(object):
    def __init__(self, n):
        self.idx = 0
        self.n = n

    def __iter__(self):
        return self

    def next(self):
        if self.idx < self.n:
            val = self.idx
            self.idx += 1
            return val
        else:
            raise StopIteration()

myRange = MyRange(3)
print isinstance([], Iterable)  # True
print isinstance([], Iterator)  # False
print isinstance(MyRange, Iterable)  # False
print isinstance(MyRange, Iterator)  # False
print isinstance(myRange, Iterable)  # True
print isinstance(myRange, Iterator)  # True


print [i for i in myRange]
print [i for i in myRange]

# 一个迭代器无法多次使用。为了解决这个问题，可以将可迭代对象和迭代器分开自定义：


class Zrange(object):
    def __init__(self, n):
        self.n = n

    def __iter__(self):
        return ZrangeIterator(self.n)


class ZrangeIterator:
    def __init__(self, n):
        self.i = 0
        self.n = n

    def __iter__(self):
        return self

    def next(self):
        if self.i < self.n:
            j = self.i
            self.i += 1
            return j
        else:
            raise StopIteration()

zrange = Zrange(3)
print zrange is iter(zrange)
print type(zrange)
print isinstance(zrange, Iterator)
print isinstance(zrange, Iterable)
print [i for i in zrange]
print [i for i in zrange]
