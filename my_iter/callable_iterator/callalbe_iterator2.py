# -*- coding: utf-8 -*-


class Itr(object):
    def __init__(self):
        self.i = 0

    def __call__(self):
        self.i = self.i + 1
        return self.i


itr = Itr()
itr_call = iter(itr, 5)
for i in itr_call:
    print i
