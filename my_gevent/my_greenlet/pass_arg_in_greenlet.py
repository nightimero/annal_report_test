# -*- coding: utf-8 -*-
from greenlet import greenlet


def my_func1(name):
    print name


gr1 = greenlet(my_func1)
gr1.switch("test_name")
