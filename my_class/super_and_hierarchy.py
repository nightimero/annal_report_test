# -*- coding:utf-8 -*-
# todo: http://www.cnblogs.com/dkblog/archive/2011/02/24/1980654.html super可以保证父类只调用一次。try
from functools import wraps


def deractor(func):
    @wraps(func)  # 加上这句话，不加这一句都是可以的。
                  # 肯定啊。wraps作用是在外部获得函数名。
    def wrap(*args):
        print "func name is:", func.__name__
        func(*args)
    return wrap


class A(object):
    def print_a(self):
        print "print_a"


class B(A):
    @deractor
    def print_b(self):
        super(B, self).print_a()


b = B()
b.print_b()
print b.print_b.__name__  # 可是在外部获取函数名有意义吗？
