# -*- coding:utf-8 -*-
# fff
# todo:为什么每一个对象都是callable的呢？

# todo： 使用类装饰器。__call__装饰。 被装饰函数，调用类中的其他方法。因为其他方法也是类的熟悉的嘛。

class Abc():
    def __init__(self,inp='test'):
        self.inp = inp

    def __call__(self,func):
        def wrap(*args,**kwargs):
            print "inner property is:",self.pp()
            print "{}".format(func.__name__)
            func(*args,**kwargs)
        return wrap

# todo: 使用对象中的方法来作为装饰器。必须要先实例化
    def deractor(self,func):
        def wrap(*args,**kwargs):
            print "inner property is:",self.pp()
            print "{}".format(func.__name__)
            func(*args,**kwargs)
        return wrap

# todo：使用对象中的方法，如果是类方法，可以实例化，也可以不实例化
# 参考： http://python3-cookbook.readthedocs.io/zh_CN/latest/c09/p08_define_decorators_as_part_of_class.html
    @classmethod
    def deractor2(cls,func):
        def wrap(*args,**kwargs):
            # print "inner property is:",cls.pp()
            # print "inner property is:", cls.inp
            # #因为该方法不是类方法，所以无法调用
            # 所以尽量用实例的装饰器。用类装饰器，最好是实现__call__的方式。
            print "{}".format(func.__name__)
            func(*args,**kwargs)
        return wrap


    def pp(self):
        return self.inp


@Abc(inp='tt')
def do_something(word):
    print "say {}".format(word)

# do_something("hi")


# @Abc().deractor # 这样调用是不行的。需要先实例化 因为deractor不是类方法。
a = Abc()
@a.deractor
def do_something2(word):
    print "say {}".format(word)

# do_something2("hi")

a = Abc()
@a.deractor2
def do_something2(word):
    print "say {}".format(word)

do_something2("hi")


@Abc.deractor2
def do_something3(word):
    print "say {}".format(word)

do_something3("hi")



