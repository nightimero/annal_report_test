# -*- coding:utf-8 -*-
# 静态方法必须用装饰器 staticmethod、classmethod 包装一下，否则会被当做实例方法
class User(object):
    pass


def mstatic(): print "static method"

User.mstatic = staticmethod(mstatic) # 使用装饰器包装。

print User.mstatic     # 正常的静态方法。<function mstatic at 0x10c88e398>

User.mstatic()     # 调用正常。static method

def cstatic(cls):     # 注意 classmethod 和 staticmethod 的区别。
    print "class method:", cls

User.cstatic = classmethod(cstatic)

print User.cstatic     # classmethod 绑定到类型对象。<bound method type.cstatic of <class '__main__.User'>>

User.cstatic()     # 调用成功。class method: <class '__main__.User'>
