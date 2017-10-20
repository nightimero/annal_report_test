# -*- coding:utf-8 -*-

# todo: http://www.cnblogs.com/dkblog/archive/2011/02/24/1980654.html super可以保证父类只调用一次。try


def deractor(func):
    def wrap(*args):
        print "func name is:", func.__name__
        func(*args)
    return wrap


class A(object):
    def print_a(self):
        print "print_a"


class B(A):
    @deractor
    def print_a(self):
        super(B, self).print_a()

# a = A()
# a.print_a()


b = B()
b.print_a()
