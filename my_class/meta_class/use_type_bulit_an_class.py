# -*- coding:utf-8 -*-
# type 的三个参数分别是：
#
# name: 要生产的类名
# bases：包含所有基类的 tuple
# dict：类的所有属性，是键值对的字典
# 现在再回顾一下 “python 中一切皆对象”这句话，可能会更容易理解。

class Foo(object):
    """A class that does nothing."""

    def __init__(self):
        self.a = 1

    def magic(self):
        return self.a

#
# 使用
# type
# 也可以做到同样的效果：


def __init__(self):
    self.a = 1


def magic(self):
    return self.a


Foo = type('Foo', (object,), {"__doc__": "A class that does nothing.", "__init__": __init__, "magic": magic})

foo = Foo()
print foo
print foo.a  # 1
print foo.magic  # <bound method Foo.magic of <__main__.Foo object at 0x100fa5d50>>
print foo.magic()  # 1
