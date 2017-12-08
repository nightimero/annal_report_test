# -*- coding: utf-8 -*-
class MetaClass(type):
    def __call__(self, *args, **kwargs):
        print('in MetaClass __call__, self id:%d' % id(self))
        a = type.__call__(self, *args, **kwargs)
        print('in MetaClass __call__, obj return from __call__:%d' % id(a))


class B(object):
    # __metaclass__ = MetaClass

    def __new__(cls, *args, **kwargs):
        print('in B __new__, cls id:%d' % id(cls))
        return super(B, cls).__new__(cls, *args, **kwargs)

    def __call__(self, *args, **kwargs):
        print 'test_call'

    def __init__(self, *args, **kwargs):
        print('in B __init__, obj id:%d' % id(self))

print type(B)  # 已经不是object类了。
print('B id:%d' % id(B))
B()
B()  # 就没有调用B自己的call方法。
a =B()
a()
