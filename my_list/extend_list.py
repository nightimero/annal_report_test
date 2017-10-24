# -*- coding:utf-8 -*-
a = ['case1', 'case2', 'case3', 'case4', 'case6', ]


class AB(list):
    def __init__(self, a):
        super(AB, self).__init__(a)

ab = AB(a)

print ab
# [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
print ab[1]
print ab.__getslice__(1, 3)


def gen_a():
    for i in range(5):
        yield i

a = gen_a()
print a.next()
print a.next()
print a.next()
print a.next()

ac = AB(gen_a())  # use generate to create a list_like object
print ac
