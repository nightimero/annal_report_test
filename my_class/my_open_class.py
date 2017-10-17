# -*- coding:utf-8 -*-
# 开放类
import types


class User(object):
    pass


def print_id(self):
    print hex(id(self))

u = User()

u.print_id = print_id   # 添加到 instance.__dict__

print u.__dict__  # {'print_id': <function print_id at 0x10c88e320>}

try:
    u.print_id()     # 失败，不是 bound method。
except TypeError as e:
    print e.message  # TypeError: print_id() takes exactly 1 argument (0 given)

u.print_id(u)     # 仅当做一个普通函数字段来用。
# 0x10c91c0d0

# 两种方法解决这个问题。
# 一、讲方法绑定到类上。
# 二、使用types.metheodtype来绑定到实例上。
print '=============2=============='


class User2(object):
    pass


def print_id2(self):
    print hex(id(self))

u = User2()

u.print_id2 = types.MethodType(print_id2, u, User2)   # 使用types.method来绑定实例方法。

print u.__dict__
# {'print_id2': <bound method User2.print_id2 of
#  <__main__.User2 object at 0x0000000003768E80>>}

u.print_id2()

print '=========3=================='


class User3(object):
    pass


def print_id3(self):
    print hex(id(self))

User3.print_id3 = print_id3  # 使用types.method来绑定实例方法。

print u.__dict__  # {'print_id2': <bound method User2.print_id2 of
                   # <__main__.User2 object at 0x0000000003768E80>>}
u = User3()

u.print_id3()
