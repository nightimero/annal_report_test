# -*- coding:utf-8 -*-
# 子类可以继承静态方法和类方法



class AA(object):
    @staticmethod
    def print_a():
        print 'hello'

    @classmethod
    def print_b(cls):
        print cls.__name__

class BB(AA):
    pass

bb = BB()
bb.print_a()
bb.print_b()
