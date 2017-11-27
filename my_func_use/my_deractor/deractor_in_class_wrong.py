# -*- coding:utf-8 -*-
class AA():
    def __init__(self):
        self.a = 'testa'
        self.b = 'testb'

    @staticmethod
    def deractor(a, b):
        def wrap(func):
            def innerwrap(*args, **kwargs):
                print "a and b is ", a, b
                func(*args, **kwargs)
            return innerwrap
        return wrap

    @deractor(self.a, self.b)  # 用了static的方法就不能调用内部的self变量
    def print_hello(self):    # 可以将self.a self.b 放到每个实例对于的配置文件中去。
        print "hello world"    # 也可以将装饰器单独作为一个类。

    @classmethod
    def print_class_name(cls):
        print cls.__name__

