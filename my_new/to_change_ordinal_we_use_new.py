# -*- coding:utf-8 -*-
# 依照Python官方文档的说法，__new__方法主要是当你继承一些不可变的class时(比如int, str, tuple)，
# 提供给你一个自定义这些类的实例化过程的途径。
# 还有就是实现自定义的metaclass。
# 首先我们来看一下第一个功能，具体我们可以用int来作为一个例子：
# 假如我们需要一个永远都是正数的整数类型，通过集成int，我们可能会写出这样的代码。


# 需求： 我们需要一个类，不管传入的是正数，还是负数，最终返回实例的值为正数
class PositiveInteger1(int):
    def __init__(self, value):
        # super(PositiveInteger, self).__init__(self, abs(value))  # 这样写和下面是等效的。
        super(PositiveInteger1, self).__init__(abs(value))  # 最好还是按照上一个写法来写。因为PositiveInteger3类有体现

i = PositiveInteger1(-3)
print i  # 依然返回 -3.不满足需求。


# 但运行后会发现，结果根本不是我们想的那样，我们任然得到了-3。
# 这是因为对于int这种 不可变的对象，我们只有重载int的__new__方法才能起到自定义的作用。
# 这是修改后的代码：
class PositiveInteger2(int):
    def __new__(cls, value):
        return super(PositiveInteger2, cls).__new__(cls, abs(value))

j = PositiveInteger2(-4)
print j


class PositiveInteger3(int):
    try:  # 这里用try 抓不住。在运行时，才能抓住。
        def __new__(cls, value):
            return super(PositiveInteger3, cls).__new__(abs(value))
    except TypeError as e:
        print e
try:  # 这里用try 能抓住。
    j = PositiveInteger3(-5)
except TypeError as e:
    print e


class Inch(float):
    """Convert from inch to meter"""
    def __new__(cls, arg=0.0):
        return float.__new__(cls, arg*0.0254)

print(Inch(12))
