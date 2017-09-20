# -*- coding:utf-8 -*-

class Fab(object):
    def __init__(self, max):
        self.max = max
        self.n, self.a, self.b = 0, 0, 1

    def __iter__(self):
        return self

    def next(self):
        if self.n < self.max:
            r = self.b
            self.a, self.b = self.b, self.a + self.b
            self.n = self.n + 1
            return r
        raise StopIteration()

def fab(max):
    n, a, b = 0, 0, 1
    while n < max:
        yield b
        # print b
        a, b = b, a + b
        n = n + 1

from inspect import isgeneratorfunction,isgenerator

#都是false，
print isgeneratorfunction(fab)
print isgeneratorfunction(Fab)
print isgeneratorfunction(Fab(5))
print isgenerator(Fab)
print isgenerator(Fab(5))

import types

print isinstance(Fab(5),types.GeneratorType)
print isinstance(Fab(5),types.GeneratorType)
print isinstance(Fab,types.GeneratorType)
print isinstance(fab(5),types.GeneratorType)

#todo: 通过debug itchat 练习读源码。