# -*- coding:utf-8 -*-
# cmp
# 
# cmp 通过返回数字来判断大小，而 eq 仅用于相等判断。


class A(object):
    def __init__(self, x):
        self.x = x

    def __eq__(self, o):
        if not o or not isinstance(o, A):
            return False
        return o.x == self.x

    def __cmp__(self, o):
        if not o or not isinstance(o, A):
            raise Exception()
        return cmp(self.x, o.x)

print A(1) == A(1)  # True
print A(1) == A(2)  # False
print A(1) < A(2)  # True
print A(1) <= A(2)  # True
