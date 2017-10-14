# -*- coding:utf-8 -*-


# 当你没有重载这个方法(通俗来说，你没有在Foo类中没有写__new__方法)，
# Foo实例化是默认自动调用父类__new__方法，这个方法返回值为类的实例(self),
# 提供这个函数how_much_of_book，默认的第一个参数self。
class Foo(object):
    price = 50

    def __new__(cls, *agrs, **kwds):
        inst = object.__new__(cls, *agrs, **kwds)
        print(inst)
        return inst

    def how_much_of_book(self, n):
        print(self)
        return self.price * n

foo = Foo()
print foo.how_much_of_book(8)


class Foo3(object):
    """
    代码写的不规范，去掉了多余的参数，方法改为类方法，因为读取的是类变量。
    """
    price = 50

    def __new__(cls):
        inst = object.__new__(cls)
        print(inst)
        return inst

    @classmethod
    def how_much_of_book(cls, n):
        print(cls)
        return cls.price * n

foo3 = Foo3()
print foo3.how_much_of_book(8)


class Foo4(object):
    def __new__(cls, *args):
        inst = object.__new__(cls)
        print(inst)
        return inst

    def __init__(self, price=50):
        self.price = price

    def how_much_of_book(self, n):
        print(self)
        return self.price * n

foo4 = Foo4(30)
print(foo4.how_much_of_book(8))

