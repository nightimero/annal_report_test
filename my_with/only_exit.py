# -*- coding:utf-8 -*-
class A(object):
    def __init__(self, value):
        print "in_init"
        self._value = value

    # 没有enter会报错。with enter exit 是一起使用的。

    def __enter__(self):
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        print 'in_exit'

    def print_value(self):
        print 'value is:', self._value

aa = A(2)
aa.print_value()

with A(2) as p:
    p.print_value()
