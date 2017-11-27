# -*- coding: utf-8 -*-
# 处理自己的数据类型
#
# json模块不仅可以处理普通的python内置类型，也可以处理我们自定义的数据类型，而往往处理自定义的对象是很常用的。
#
# 首先，我们定义一个类Person。
#

class Person(object):
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def __repr__(self):
        return 'Person Object name : %s , age : %d' % (self.name, self.age)


if __name__ == '__main__':
    p = Person('Peter', 22)
    print p
# 如果直接通过json.dumps方法对Person的实例进行处理的话，会报错，因为json无法支持这样的自动转化。通过上面所提到的json和python的类型转化对照表，可以发现，object类型是和dict相关联的，所以我们需要把我们自定义的类型转化为dict，然后再进行处理。这里，有两种方法可以使用。
#
# 方法一：自己写转化函数

'''
Created on 2011-12-14
@author: Peter
'''
# import Person
import json

p = Person.Person('Peter', 22)


def object2dict(obj):
    # convert object to a dict
    d = {}
    d['__class__'] = obj.__class__.__name__
    d['__module__'] = obj.__module__
    d.update(obj.__dict__)
    return d


def dict2object(d):
    # convert dict to object
    if '__class__' in d:
        class_name = d.pop('__class__')
        module_name = d.pop('__module__')
        module = __import__(module_name)
        class_ = getattr(module, class_name)
        args = dict((key.encode('ascii'), value) for key, value in d.items())  # get args
        inst = class_(**args)  # create new instance
    else:
        inst = d
    return inst


d = object2dict(p)
print d
# {'age': 22, '__module__': 'Person', '__class__': 'Person', 'name': 'Peter'}

o = dict2object(d)
print type(o), o
# <class 'Person.Person'> Person Object name : Peter , age : 22

dump = json.dumps(p, default=object2dict)
print dump
# {"age": 22, "__module__": "Person", "__class__": "Person", "name": "Peter"}

load = json.loads(dump, object_hook=dict2object)
print load
# Person Object name : Peter , age : 22
# 上面代码已经写的很清楚了，实质就是自定义object类型和dict类型进行转化。object2dict函数将对象模块名、
# 类名以及__dict__存储在dict对象里，并返回。dict2object函数则是反解出模块名、类名、参数，创建新的对象并返回。在json.dumps
# 方法中增加default参数，该参数表示在转化过程中调用指定的函数，同样在decode过程中json.loads方法增加object_hook, 指定转化函数。
#
# 方法二：继承JSONEncoder和JSONDecoder类，覆写相关方法
#
# JSONEncoder类负责编码，主要是通过其default函数进行转化，我们可以override该方法。同理对于JSONDecoder。

'''
Created on 2011-12-14
@author: Peter
'''
# import Person
import json

p = Person.Person('Peter', 22)


class MyEncoder(json.JSONEncoder):
    def default(self, obj):
        # convert object to a dict
        d = {}
        d['__class__'] = obj.__class__.__name__
        d['__module__'] = obj.__module__
        d.update(obj.__dict__)
        return d


class MyDecoder(json.JSONDecoder):
    def __init__(self):
        json.JSONDecoder.__init__(self, object_hook=self.dict2object)

    def dict2object(self, d):
        # convert dict to object
        if '__class__' in d:
            class_name = d.pop('__class__')
            module_name = d.pop('__module__')
            module = __import__(module_name)
            class_ = getattr(module, class_name)
            args = dict((key.encode('ascii'), value) for key, value in d.items())  # get args
            inst = class_(**args)  # create new instance
        else:
            inst = d
        return inst


d = MyEncoder().encode(p)
o = MyDecoder().decode(d)

print d
print type(o), o

# 对于JSONDecoder类方法，稍微有点不同，但是改写起来也不是很麻烦。看代码应该就比较清楚了。
