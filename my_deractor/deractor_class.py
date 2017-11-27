# -*- coding:utf-8 -*-
# http://www.wklken.me/posts/2012/10/27/python-base-decorator.html

# 装饰器分类


# 一、无参数装饰器 – 包装无参数函数 # 一个def
# 不需要对被装饰的函数进行处理和优化
def decorator(func):
    print "hello"
    return func


@decorator
def foo():
    pass


foo()


# 二、无参数装饰器 – 包装带参数函数 # 两个def

def decorator_func_args(func):
    def handle_args(*args, **kwargs):  # 处理传入函数的参数
        print "begin"
        func(*args, **kwargs)  # 函数调用
        print "end"

    return handle_args


@decorator_func_args
def foo2(a, b=2):
    print a, b


foo2(1)


# 三、带参数装饰器 – 包装无参数函数 # 两个def
def decorator_with_params(arg_of_decorator):  # 这里是装饰器的参数
    print arg_of_decorator

    # 最终被返回的函数
    def new_decorator(func):
        print func
        # func()  # 如果有这个函数就会运行两次。
        return func

    return new_decorator


@decorator_with_params("deco_args")
def foo3():
    print "hello world1"


foo3()  # 因为有()，所以就是执行函数了。因为一路从底返回的是函数的引用。


# 四、带参数装饰器– 包装带参数函数 #三个def


def decorator_whith_params_and_func_args(arg_of_decorator):
    def handle_func(func):
        def handle_args(*args, **kwargs):
            print "begin"
            func(*args, **kwargs)
            print "end"
            print arg_of_decorator, func, args, kwargs

        return handle_args

    return handle_func


@decorator_whith_params_and_func_args("123")
def foo4(a, b=2):
    print "Content", a, b


foo4(1, b=3)
