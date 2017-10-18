# -*- coding:utf-8 -*-


class User: pass

print type(User)    # 2.x 默认是 Classic Class。
# <type 'classobj'>

print issubclass(User, object)  # 显然不是从 object 继承。
# False

__metaclass__ = type   # 指定默认元类。

class Manager: pass   # 还是没有显式从 object 继承。

print type(Manager)    # 但已经是 New-Style Class。
# <type 'type'>

print issubclass(Manager, object)  # 确定了！
# True
