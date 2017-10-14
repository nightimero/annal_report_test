# -*- coding:utf-8 -*-


class Data1(object):
    """
    在类中，如果__new__和__init__同时存在，会优先调用__new__
    """
    def __new__(cls):
        print "new1"

    def __init__(self):
        print "init1"

data1 = Data1()   # 打印：new1 不打印init1


class Data2(object):
    """
    __new__方法会返回所构造的对象，__init__则不会。__init__无返回值。
    """
    def __init__(self):
        self.x = 2
        print "init2"
        return self

try:
    data2 = Data2()  # TypeError: __init__() should return None, not 'Data'
except TypeError as e:
    print '==============='
    print e.message
    print e.args[0]
    print type(e)  # <type 'exceptions.TypeError'>
    print e.__doc__  # Inappropriate argument type.
    print '==============='


class Data3(object):
    def __new__(cls):
        print "new3"
        cls.x = 1
        return cls

    def __init__(self, y):
        self.y = y
        print "init3"

data3 = Data3()  # 打印 new ，不打印 init
data3.x = 1
print data3.x
try:
    print data3.y  # "type object 'Data3' has no attribute 'y'"
except AttributeError as e:
    print e.message

