# -*- coding:utf-8 -*-
# 事实上，当我们理解了__new__方法后，我们还可以利用它来做一些其他有趣的事情，
# 比如实现 设计模式中的 单例模式(singleton) 。
# 因为类每一次实例化后产生的过程都是通过__new__来控制的，
# 所以通过重载__new__方法，我们 可以很简单的实现单例模式。
from pprint import pprint


class Singleton(object):
    def __new__(cls):
        # 关键在于这，每一次实例化的时候，我们都只会返回这同一个instance对象
        if not hasattr(cls, 'instance'):
            cls.instance = super(Singleton, cls).__new__(cls)
        return cls.instance

obj1 = Singleton()
obj2 = Singleton()

obj1.attr1 = 'value1'
print obj1.attr1, obj2.attr1
print obj1 is obj2


class Singleton2(object):
    # 这个位置的才是类变量。
    brand = 'IBM'

    def __new__(cls, computer):
        # 关键在于这，每一次实例化的时候，我们都只会返回这同一个instance对象
        print computer  # 这个computer不是类变量，也不是实例变量。传给了__init__才会成为实例变量。
        if not hasattr(cls, 'instance'):
            cls.instance = super(Singleton2, cls).__new__(cls)
        return cls.instance


obj1 = Singleton2("dell")
obj2 = Singleton2("hp")

obj1.attr1 = 'value1'
print obj1.attr1, obj2.attr1
print obj1 is obj2
print obj1.brand, obj2.brand


class SingletonWithAttr1(object):
    def __new__(cls, computer):
        if not hasattr(cls, 'instance'):
            cls.instance = super(SingletonWithAttr1, cls).__new__(cls, computer)
        return cls.instance

    def __int__(self, computer):  # 因为init啊。 int啊。init啊。注意啊。
        self.computer = computer
try:  # 这里报错：object() takes no parameters
    print '===================='
    obj1 = SingletonWithAttr1("dell")
    print obj1.computer
except TypeError as e:
    print e.message


class SingletonWithAttr2(object):
    def __new__(cls, *args, **kwargs):
        if not hasattr(cls, 'instance'):
            cls.instance = super(SingletonWithAttr2, cls).__new__(cls)
        return cls.instance

    def __init__(self, computer):
        self.computer = computer
try:
    obj1 = SingletonWithAttr2("dell")
    obj2 = SingletonWithAttr2("hp")
    print obj1.computer, obj2.computer
    print obj2
    print obj2.instance
    # todo： 这里都是一样的，好奇怪 。这里是怎么循环指向的呢？
    # 这里是调用了类变量。obj2.instance  = SingletonWithAttr2.instance = obj1 = obj2
    print(dir(obj2))
    print(dir(obj2.instance))
    print(dir(obj2.instance.instance))
except TypeError as e:
    print e.message
