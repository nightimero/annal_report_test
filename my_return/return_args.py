# -*- coding:utf-8 -*-
def func_a():
    a = 1
    b = 2
    return [a, b]


def func_b():
    s = func_a()
    c = 3
    return s, c

print func_b()


def func_c(*a):
    d = 4
    return d, a

print func_c(func_a())
print func_c(1, 2)

#  说明了在format()中可以传入 *a,是因为format是个函数，接受变长参数。


def func_d(a):
    e = 5
    a.append(e)
    return a

print func_d(func_a())
