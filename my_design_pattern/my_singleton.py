# -*- coding:utf-8 -*-

#第一种方式，python天然就是单例模式，在第一次导入时，pyc直接加载，不会再执行模块代码。
# 所以需要把相关函数和数据定义在一个模块中，导入该模块就获得了一个单例类。

class My_Singleton(object):
    def foo(self):
        pass

my_singleton = My_Singleton()

#其他文件中的调用代码
from my_singleton import my_singleton
my_singleton.foo()

#第二种方法，使用 __new__和继承

class Singleton(object):
    _instances = None
    def __new__(cls, *args, **kwargs):
        if not cls._instances:
            cls._instances = super(Singleton,cls).__new__(cls,*args,**kwargs)
        return cls._instances

class Myclass(Singleton):
    a = 1

#第三种方法，使用装饰器
from functools import wraps

#todo: 找到这个instance变量和其对于的字典，应该是co_freevar,学习co_开头变量的使用 ,没有看见一个dict变量类型的局部变量。
def singleton(cls):
    instance = {}
    @wraps(cls)
    def getinstance(*args,**kwargs):
        if cls not in instance:
            instance[cls] = cls(*args,**kwargs)
        return instance[cls]
    return getinstance

#todo：类名称也可以作为字典的key？类名称是字符串？
#todo：装饰器除了装饰费方法，还可以装饰类？ 搜索下。
@singleton
class MyClass(object):
    a = 1
#使用元类 http://funhacks.net/2017/01/17/singleton/
#https://www.google.com/search?q=python%E5%8D%95%E4%BE%8B%E6%A8%A1%E5%BC%8F&oq=python%E5%8D%95%E4%BE%8B%E6%A8%A1%E5%BC%8F
# https://www.google.com/search?q=python+%E6%9F%A5%E7%9C%8B+%E6%96%B9%E6%B3%95+%E6%9C%AC%E5%9C%B0%E5%8F%98%E9%87%8F&oq=python+%E6%9F%A5%E7%9C%8B+%E6%96%B9%E6%B3%95+%E6%9C%AC%E5%9C%B0%E5%8F%98%E9%87%8F


