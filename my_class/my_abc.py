# -*- coding:utf-8 -*-
# 抽象类

from abc import ABCMeta, abstractmethod, abstractproperty


class User(object):
    __metaclass__ = ABCMeta   # 通过元类来控制抽象类行为。

    def __init__(self, uid):
        self._uid = uid

    @abstractmethod
    def print_id(self): pass  # 抽象方法

    name = abstractproperty()  # 抽象属性


class Manager(User):
    def __init__(self, uid):
        User.__init__(self, uid)

    def print_id(self):
        print self._uid, self._name

    name = property(lambda self: self._name, lambda self, v: setattr(self, "_name", v))
try:
    u = User(1)     # 抽象类无法实例化。
except TypeError as e:
    print e.message
# TypeError: Can't instantiate abstract class User with abstract methods name, print_id

m = Manager(1)
m.name = "Tom"
m.print_id()  # 1 Tom
print m._name


class Manager2(User):
    __metaclass__ = ABCMeta

    def __init__(self, uid, name):
        User.__init__(self, uid)
        self.name = name

    uid = property(lambda self: self._uid)
    name = property(lambda self: self._name, lambda self, v: setattr(self, "_name", v))
    title = abstractproperty()


class CXO(Manager2):
    def __init__(self, uid, name):
        Manager2.__init__(self, uid, name)

    def print_id(self):
        print self.uid, self.name, self.title

    title = property(lambda self: "CXO")

c = CXO(1, "Tom")
c.print_id()  # 1 Tom CXO
