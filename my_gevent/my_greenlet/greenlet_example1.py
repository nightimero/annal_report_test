# -*- coding: utf-8 -*-
from greenlet import greenlet


def my_func1():
    print "my_func1-1"
    gr2.switch()
    print "my_func1-2"


def my_func2():
    print "my_func2-1"
    return "fjsfjsfjs"


gr1 = greenlet(my_func1)
gr2 = greenlet(my_func2)

out = gr1.switch()  # 启动greenlet
print out
