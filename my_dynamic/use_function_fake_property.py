# -*- coding:utf-8 -*-

# 用方法冒充字段:
# 　　有时候，我们的一个方法在经过一系列处理以后，返回的是一个数据，例如：
# class Test:
#
#     def __init__(self, a, b):
#         self.a = a
#         self.b = b
#
#     def fangfa(self):
#         c = self.a + self.b
#         return c    # 返回处理的结果数据
#
#
# a = Test(1, 2)
# b = a.fangfa()    # 调用方法,得到返回值
# print b
#
# 但是，懒惰的程序员们想：我想要的只是和字段类似的数据，却要调用一个方法，有时候容易搞错，能不能用字段的形式获取数据呢？这样更加符合直觉。
#
# 　　可以，只有使用 property() 函数就可以了。同样的，这里也有两种创建方式，这里只演示装饰器的方式：

class Test:

    def __init__(self, a, b):
        self.a = a
        self.b = b

    @property
    def fangfa(self):
        c = self.a + self.b
        return c


a = Test(1, 2)
b = a.fangfa    # 不用带括号了
print b


# 　这样是实现了方法伪装成字段了。其实就是懒惰的程序员们不愿意多写一个括号，当然还有一些其他好处。
#
# 　　另外，函数要用返回值，不然就默认为 None 了。
#
# 　　如果在经典类中，我们就只能做到这样了。
#
# 　　但是，使用新式类的话，就能有更多的功能：


class Test(object):

    def __init__(self, a, b):
        self.a = a
        self.b = b

    @property
    def fangfa(self):
        c = self.a + self.b
        return c

    @fangfa.setter
    def fangfa(self, value):
        self.a = value

    @fangfa.deleter
    def fangfa(self):
        print '属性已删除'

a = Test(1, 2)
b = a.fangfa   # 获得方法的返回值
print b
a.fangfa = 100    # 执行 fangfa.setter 修饰的方法，并让value = 100
print a.a
del a.fangfa    # 执行 fangfa.deleter 修饰的方法

#
# 　注意后面两个装饰器的名字。
#
# 　　另外，方法必须要先经过 property()函数的装饰后，才有后面两个装饰器的用法。
#
# 　　如果使用非装饰器的形式的话：


class Test(object):

    def __init__(self, a, b):
        self.a = a
        self.b = b

    def fangfa_get(self):
        c = self.a + self.b
        return c

    def fangfa_set(self, value):
        self.a = value

    def fangfa_del(self):
        print '属性已删除'

    fangfa = property(fangfa_get, fangfa_set, fangfa_del)
