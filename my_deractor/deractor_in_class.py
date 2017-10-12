# -*- coding:utf-8 -*-


class AA:
    def __init__(self):
        self.a = 'testa'
        self.b = 'testb'

    @staticmethod
    def deractor1(a, b):
        def wrap(func):
            def innerwrap(*args, **kwargs):
                print "a and b is ", a, b
                func(*args, **kwargs)
            return innerwrap
        return wrap

    def deractor2(self):
        def wrap(func):
            def innerwrap(*args, **kwargs):
                print "a and b is ", self.a, self.b
                func(*args, **kwargs)
            return innerwrap
        return wrap

    # 不能再父类中装饰
    def print_hello(self):
        print "hello world"

    @classmethod
    def print_class_name(cls):
        print cls.__name__


class BB(AA):
    @AA.deractor1(3,5)
    def print_hello(self):
        super()