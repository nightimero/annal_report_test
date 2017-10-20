# -*- coding:utf-8 -*-
import sys
import inspect
list_a = ['age', 'name']


class B(object):
    def __init__(self, str_b):
        print 'hello ' + str_b

module1 = sys.modules[__name__]
print module1
_class = inspect.getmembers(module1, inspect.isclass)[0][0]


class AC(object):
    def __init__(self, value, str_b):
        self.__setattr__(list_a[0], value)
        self.__setattr__('b', _class(str_b))

    def __getattr__(self, item):
        return self.__dict__[item]

    def __setattr__(self, key, value):
        self.__dict__[key] = value


module1 = sys.modules[__name__]
print module1
_class = inspect.getmembers(module1, inspect.isclass)[1][1]
ac = AC(13, 'bbb')
# attr_age = list_a[0]
# ac.attr_age = 12
# print ac.age
# ac.__setattr__('age', '12')
# print ac.__getattr__('age')

# ac.__setattr__(list_a[0], '12')
print ac.__getattr__('age')
print ac.age




# ==============错误的写法=====================

#
# class AB(object):
#     global list_a
#
#     def __init__(self, value):
#         self.list_a[0] = value
#
# ab = AB(12)
# print ab.list_a[0]
# ==============错误的写法=====================
