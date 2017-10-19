# -*- coding:utf-8 -*-
import inspect
import os
from pprint import pprint
# inspect.getmodule()

print 'inspect.isbuiltin abs:', inspect.isbuiltin(abs)  # True
print 'inspect.isbuiltin os:', inspect.isbuiltin(os)  # False
print 'inspect.ismodudle os:', inspect.ismodule(os)  # True


class C(object):
    pass

print 'inspcet.isclass C:', inspect.isclass(C)  # True


class AB(object):
    attr = 'xxx'

    def foo(self):
        pass

    def bez(self):
        pass

print 'inspect.getmembers:', inspect.getmembers(AB, inspect.ismethod)
# [('bez', <unbound method AB.bez>), ('foo', <unbound method AB.foo>)]
print 'inspect.getmembers:'
pprint(inspect.getmembers(AB))

