# -*- coding:utf-8 -*-
import sys
import inspect


class A(object):
    pass


def print_classes():
    for name, obj in inspect.getmembers(sys.modules[__name__]):
        if inspect.isclass(obj):
            print(obj)

print_classes()
