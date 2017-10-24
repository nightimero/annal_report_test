# -*- coding:utf-8 -*-
# call
# 
# 像函数那样调用对象，也就是传说中的 callable。


class A(object):
    def __call__(self, *args, **kwargs):
        print hex(id(self)), args, kwargs

a = A()

a(1, 2, s="hi")
# 完全可以把对象实例伪装成函数接口。
# 0x10c8957d0 (1, 2) {'s': 'hi'}
