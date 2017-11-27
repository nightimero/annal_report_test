# -*- coding:utf-8 -*-


class AA(object):  # 如果不是新式类的话。子类还不能用super。 提示子类不是type，是classobj
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
        def deractor(func):
            def wrap(*args, **kwargs):
                func(*args, **kwargs)
                print cls.__name__
                return wrap
            return deractor

class BB(AA):
    @AA.deractor1(3, 5)
    def print_hello(self):
        super(BB, self).print_hello()

    @AA.print_class_name  # TypeError: print_class_name() takes exactly 1 argument (2 given) 没有这样写的。deractor_in_class.py
    def print_world(self):
        print 'this is world'

bb = BB()
bb.print_hello()
bb.print_world()
