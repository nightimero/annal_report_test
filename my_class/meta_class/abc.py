# -*- coding:utf-8 -*-
# 参考： http://cizixs.com/2015/08/30/metaclass-in-python


class MyMetaClass(type):
    def __new__(cls, name, bases, attrs):
        attrs['__cizixs'] = "Don't panic"
        print("In MyMetaclass for {}".format(name))
        return super(MyMetaClass, cls).__new__(cls, name, bases, attrs)


class Foo(object):
    __metaclass__ = MyMetaClass

    pass


# In MyMetaclass for Foo

foo = Foo()
print foo.__cizixs  # Don't panic


class MyMetaClass2(type):
    def __init__(cls, name, bases, attrs):
        # attrs['__cizixs'] = "Don't panic"  # 这样写是错误的。
        cls.cizixs = "Don't panic"
        cls.__cizixs2 = 'class panic'
        print("In MyMetaclass for {}".format(name))
        super(MyMetaClass2, cls).__init__(name, bases, attrs)


class Foo2(object):
    __metaclass__ = MyMetaClass2

    pass

# In MyMetaclass for Foo

foo2 = Foo2()
print foo2.cizixs  # Don't panic
try:
    print foo2._Foo2__cizixs2
except AttributeError as e:
    print e

print foo2._MyMetaClass2__cizixs2  # 居然不是 _Foo2__cizixs2
print dir(foo2)
