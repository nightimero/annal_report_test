# -*- coding:utf-8 -*-
import inspect
from pprint import pprint


def f():
    pprint(inspect.stack())
    x = 1
    return x


def g():
    y = f()
    return y
if __name__ == '__main__':
    g()

