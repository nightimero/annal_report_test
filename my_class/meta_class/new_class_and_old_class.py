# -*- coding:utf-8 -*-
from types import ClassType


class User: pass


print type(User)  # 2.x 默认是 Classic Class。
# <type 'classobj'>  这是旧式类

print issubclass(User, object)  # 显然不是从 object 继承。
# False

print "is classobj:", isinstance(User, ClassType)

__metaclass__ = type  # 指定默认元类。
# __metaclass__ = object  # 指定默认元类。  不能这样写。
# TypeError: Error when calling the metaclass bases
# object() takes no parameters



class Manager: pass  # 还是没有显式从 object 继承。


print type(Manager)  # 但已经是 New-Style Class。
# <type 'type'>

print issubclass(Manager, object)  # 确定了！
# True
