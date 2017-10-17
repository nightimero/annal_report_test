# -*- coding:utf-8 -*-
# slots
# slots 属性会阻止虚拟机创建实例 dict，仅为名单中的指定成员分配内存空间。
# 这有助于减少内存占用，提升执行性能，尤其是在需要大量此类对象的时候。
import inspect


class User(object):
    __slots__ = ("_name", "_age")

    def __init__(self, name, age):
        self._name = name
        self._age = age

u = User("Tom", 34)

hasattr(u, "__dict__")  # False

try:
    u.title = "CXO"    # 动态增加字段失败。
except AttributeError as e:
    print e.message  # AttributeError: 'User' object has no attribute 'title'

del u._age     # 已有字段可被删除。
u._age = 18     # 将坑补回是允许的。
print u._age  # 18

try:
    vars(u)      # 因为没有 __dict__，vars 失败。
except TypeError as e:
    print e.message
# TypeError: vars() argument must have __dict__ attribute
# 虽然没有了 dict，但依然可以用 dir() 和 inspect.getmembers() 获取实例成员信息。


u = User("Tom", 34)

print {k: getattr(u, k) for k in dir(u) if not k.startswith("__")}  # {'_age': 34, '_name': 'Tom'}

print {k: v for k, v in inspect.getmembers(u) if not k.startswith("__")}  # {'_age': 34, '_name': 'Tom'}
# 其派生类同样必须用 slots 为新增字段分配存储空间 (即便是空 slots = [])，否则依然会创建 dict，反而导致更慢的执行效率。


class Manager(User):
    __slots__ = ("_title")

    def __init__(self, name, age, title):
        User.__init__(self, name, age)
        self._title = title

    def print_man(self):
        print self._name,self._age,self._title

m1 = Manager('luke', 15, 'CTO')
m1.print_man()
