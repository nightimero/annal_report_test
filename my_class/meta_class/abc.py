# -*- coding:utf-8 -*-
# 参考： http://cizixs.com/2015/08/30/metaclass-in-python


class MyMetaClass(type):
    def __new__(cls, name, bases, attrs):
        attrs['__cizixs'] = "Don't panic"
        print("In MyMetaclass for {}".format(name))
        cls.__test = 'test_attr'
        return super(MyMetaClass, cls).__new__(cls, name, bases, attrs)
        # return type.__new__(cls, name, bases, attrs)  也可以这样写。 本来这个类的父类就是type元类


class Foo(object):
    __metaclass__ = MyMetaClass

    pass


# In MyMetaclass for Foo

foo = Foo()
print foo.__cizixs  # Don't panic
print Foo.__cizixs  # Don't panic
print 'dir(foo)', dir(foo)
# print 'MyMetaClass', foo.MyMetaClass.__test  # 这样是错的。
# print dir(foo.__metaclass__)
# 它的metaclass中有MyMetaClass.__test这个属性。 且是个私有属性。
print foo.__metaclass__._MyMetaClass__test

class MyMetaClass2(type):
    def __init__(cls, name, bases, attrs):
        # attrs['__cizixs'] = "Don't panic"  # 这样写是错误的。
        cls.cizixs = "Don't panic"
        cls.__cizixs2 = 'class panic'
        attrs['test2'] = 'testabc'
        print("In MyMetaclass for {}".format(name))
        super(MyMetaClass2, cls).__init__(name, bases, attrs)


class Foo2(object):
    __metaclass__ = MyMetaClass2

    pass

# In MyMetaclass for Foo

foo2 = Foo2()
print foo2.cizixs  # Don't panic
print Foo2.cizixs  # Don't panic
try:
    print foo2._Foo2__cizixs2
except AttributeError as e:
    print e

print foo2._MyMetaClass2__cizixs2  # 居然不是 _Foo2__cizixs2,肯定啊，是元类啊。
print dir(foo2)
print foo2.test2  # 在init中就不能用attrrs来构造属性了。已经开始实例化了。
