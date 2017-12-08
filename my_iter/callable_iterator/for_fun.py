# -*- coding: utf-8 -*-
class Itr(object):
    def __init__(self):
        self.result = ['a', 'b', 'c', 'd']
        self.i = iter(self.result)

    def __call__(self):
        res = next(self.i)
        print("__call__ called, which would return ", res)
        return res+'d'

    def __iter__(self):
        print("__iter__ called")
        return iter(self.result)


itr = Itr()
# i1必须是callable的，否则无法返回callable-iterator
i1 = iter(itr, 'cd')
print("i1 = ", i1)

for i in i1:
    print(i)
