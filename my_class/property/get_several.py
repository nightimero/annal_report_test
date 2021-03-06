# -*- coding:utf-8 -*-
# getattr
# 
# 先看看这几个方法的触发时机。
# 
# getattr: 访问不存在的成员。
# setattr: 对任何成员的赋值操作。
# delattr: 删除成员操作。
# getattribute: 访问任何存在或不存在的成员，包括 dict。
# 不要在这几个方法里直接访问对象成员，也不要用 hasattr/getattr/setattr/delattr 函数，
# 因为它们会被再次拦截，形成无限循环。正确的做法是直接操作 dict。
# 
# 而 getattribute 连 dict 都会拦截，只能用基类的 getattribute 返回结果。


class A(object):
    def __init__(self, x):
        self.x = x    # 会被 __setattr__ 捕获。

    def __getattr__(self, name):
        print "get:", name
        # 下面这句话就是废话。完全是画蛇添足，再去获取一次属性。
        return self.__dict__.get(name)

    def __setattr__(self, name, value):
        print "set:", name, value
        self.__dict__[name] = value

    def __delattr__(self, name):
        print "del:", name
        self.__dict__.pop(name, None)

    def __getattribute__(self, name):
        print "attribute:", name
        return object.__getattribute__(self, name)

a = A(10)   # __init__ 里面的 self.x = x 被 __setattr__ 捕获。
# set: x 10
# attribute: __dict__

a.x    # 访问已存在字段，仅被 __getattribute__ 捕获。
# attribute: x
# 10

a.y = 20   # 创建新的字段，被 __setattr__ 捕获。
# set: y 20
# attribute: __dict__
print '==========a.z'
a.z    # 访问不存在的字段，被 __getattr__ 捕获。
# attribute: z
# get: z
# attribute: __dict__
print '==========a.z'
del a.y    # 删除字段被 __delattr__ 捕获。
# del: y
# attribute: __dict__


# todo: http://blog.csdn.net/qdx411324962/article/details/48000651  __get__什么意思?
# todo: http://www.jianshu.com/p/885d59db57fc  这是什么意思？
# 3.同时覆盖掉getattribute和getattr的时候，在getattribute中需要模仿原本的行为抛出AttributeError或者手动调用getattr