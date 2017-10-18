# -*- coding:utf-8 -*-
# iter函数有两种用法，一种是传一个参数，一种是传两个参数。返回的结果都是返回一个iterator对象。
# 先说传两个参数的，比如有

# 一、

# def itr():
#     pass
#
# i1 = iter(itr, 'c')

# 这个意思是说，返回itr的iterator，而且在之后的迭代之中，迭代出来'c'就立马停止。
# 对这个itr有什么要求呢？这个itr在这里必须是callable的，即要实现__call__函数


# 二、这里itr必须实现__iter__函数，这个函数的返回值必须返回一个iterator对象

# i2 = iter(itr)


class Itr(object):
    def __init__(self):
        self.result = ['a', 'b', 'c', 'd']
        self.i = iter(self.result)

    def __call__(self):
        res = next(self.i)
        print("__call__ called, which would return ", res)
        return res

    def __iter__(self):
        print("__iter__ called")
        return iter(self.result)


itr = Itr()
# i1必须是callable的，否则无法返回callable-iterator
i1 = iter(itr, 'c')
print("i1 = ", i1)
# i2只需要类实现__iter__函数即可返回
i2 = iter(itr)
print("i2 = ", i2)

for i in i1:
    print(i)

for i in i2:
    print(i)


class Next(object):
    def __init__(self, data=1):
        self.data = data

    def __iter__(self):
        return self

    def next(self):    # python2 用next。python3 用__next__
        print("__next__ called")
        if self.data > 5:
            raise StopIteration
        else:
            self.data += 1
            return self.data

for i in Next(3):
    print(i)

bb = Next(4)
print bb.next()  # python2 用next。python3 用__next__
print bb.next()
print bb.next()
