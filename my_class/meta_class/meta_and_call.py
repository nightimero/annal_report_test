# -*- coding: utf-8 -*-
# todo: http://www.cnblogs.com/pengyusong/p/6838407.html
# todo: https://stackoverflow.com/questions/100003/what-is-a-metaclass-in-python google 搜索 python metaclass
# todo: https://eli.thegreenplace.net/2011/08/14/python-metaclasses-by-example   google 搜索 metaclass init call
# todo： call in metaclass
class SuperMeta(type):
    def __call__(metaname, clsname, baseclasses, attrs):
        print 'SuperMeta Called'
        clsob = type.__new__(metaname, clsname, baseclasses, attrs)
        type.__init__(clsob, clsname, baseclasses, attrs)
        return clsob


class MyMeta(type):
    __metaclass__ = SuperMeta

    def __call__(cls, *args, **kwargs):
        print 'MyMeta called', cls, args, kwargs
        ob = object.__new__(cls, *args)
        ob.__init__(*args)
        return ob


print 'create class'


class Kls(object):
    __metaclass__ = MyMeta

    def __init__(self, data):
        self.data = data

    def printd(self):
        print self.data


print 'class created ---------------------'
# 你会发现定义了 Kls 类后输出了 SuperMeta 父元类的输出
ik = Kls('arun')
ik.printd()
ik2 = Kls('avni')

ik2.printd()
# 定义Kls对象实例才真的执行了MyMeta的call
