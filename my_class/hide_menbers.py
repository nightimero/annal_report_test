# -*- coding:utf-8 -*-
# dir
# 
# 配合 slots 隐藏内部成员。


class A(object):
    __slots__ = ("x", "y")

    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __dir__(self):
        # 必须返回 list，而不是 tuple。
        # 这里的dir可以是静态方法
        return ["x"]

a = A(1, 2)

print dir(a)     # y 不见了。['x']
print dir(A)


class B(object):
    # __slots__ = ("x", "y")  # 没有slot，dir（class）不会返回属性。

    def __init__(self, x, y):
        self.x = x
        self.y = y

    @staticmethod
    def __dir__():  # 必须返回 list，而不是 tuple。
        return ["x"]

b = B(1, 2)

print dir(b)     # y 不见了。['x']
print dir(B)


class C(object):
    __slots__ = ("x", "y")

    def __init__(self, x, y):
        self.x = x
        self.y = y

    @staticmethod
    def __dir__():  # 必须返回 list，而不是 tuple。
        return ["x"]

c = C(1, 2)

print dir(c)     # y 不见了。['x']
print dir(C)
