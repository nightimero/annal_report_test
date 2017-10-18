# -*- coding:utf-8 -*-

# todo: how to infinity recursion. by getattribute
#
# 因为getattribute在访问属性的时候一直会被调用，自定义的getattribute方法里面同时需要返回相应的属性，
# 通过self.__dict__取值会继续向下调用getattribute，造成循环调用：


class AboutAttr(object):
    def __init__(self, name):
        self.name = name

    def __getattribute__(self, item):
        try:
            # 逐级向上查找类的静态字段。因为静态字段也可以被实例通过self调用。
            # 直到object对象。如果找到object了。那肯定是没有。就抛出异常。
            return super(AboutAttr, self).__getattribute__(item)
        except KeyError:
            return 'default'

a = AboutAttr('test')
print a.name
try:
    print a.xxx
except AttributeError as e:
    print e.message


class AboutAttr2(object):
    def __init__(self, name):
        self.name = name

    def __getattribute__(self, item):
        return "default"

b = AboutAttr2('tester')
print b.name  # default
print b.yyy  # default


class AboutAttr3(object):
    def __init__(self, name):
        self.name = name

    def __getattribute__(self, item):
        return self.__dict__[item]

c = AboutAttr3('tester')
try:
    print c.name
except RuntimeError as e:
    print e.message
    # RuntimeError: maximum recursion depth exceeded while calling a Python object


class AboutAttr4(object):
    def __init__(self, name):
        self.name = name

    def __getattribute__(self, item):
        return self.__dict__[item]

d = AboutAttr4('tester')
print AboutAttr4.__dict__
try:
    print d.__dict__
except RuntimeError as e:
    print e.message


class AB(object):
    sex = 'default sex'

    def __init__(self, name, age):
        self.name = name
        self.age = age

ab = AB('tom', 12)
print ab.__dict__

print '=========AC=============='


class AC(AB):
    def __init__(self, position):
        self.position = position

    def __getattribute__(self, item):
        print 'to find the attr:', item
        # try:
        #     return super(AC, self).__getattr__(item)   # 这种运算符重载就只能在类方法中使用。
        #     # AttributeError: 'super' object has no attribute '__getattr__'
        # except AttributeError as e:
        #     print e.message
        return super(AC, self).__getattribute__(item)

    def __getattr__(self, item):
        print 'in getattr'
        if item == 'tester':
            return True

ac = AC('cto')
# print ac.position
# print ac.sex
# print ac.__getattribute__('position')
# print ac.__getattribute__('sex')
# print ac.sex

# print ac.tester

try:
    print ac.__getattribute__('tester')
    # 这样的操作符.不会被重载。会导致不会被getattr捕获。导致异常
    # 只有instance.attr 这样的操作才会被重载。
except AttributeError as e:
    print e
