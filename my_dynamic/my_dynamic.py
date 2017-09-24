# -*- coding:utf-8 -*-
#task: 掉用父类中被覆盖的方法
#super 并不是父类的意思，super是一个类，返回mro的一个list https://laike9m.com/blog/li-jie-python-super,70/  print(d.__class__.__mro__)
#深入： mro关系树 http://www.cnblogs.com/lovemo1314/archive/2011/05/03/2035005.html
#深入： mro关系树 http://gohom.win/2016/02/23/py-super/

class Abc(object):
    def __init__(self, a):
        self.a = -int(a)

    def print_a(self):
        print 'hello'
        return "hello world"

class Test(Abc):
    # 这种直接使用类名的方法和下面使用super的方法是一样的。可以指定类避免多重继承的混乱。
    # 最后的最后，提醒大家. 什么 super 啊，MRO 啊，都是针对 new-style class。如果不是 new-style class，就老老实实用父类的类名去调用函数吧。
    # 这是第一种方法
    # def __init__(self, a, b):
    #     Abc.__init__(self, a)   # 调用父类的构造器，并手动传递 self
    #     self.b = b

    #这是第二种方法
    def __init__(self,a,b):
        super(Test,self).__init__(a)
        self.b = b

    #这是第三种方法 Parent ，python2中没有这个关键字 Parent.__init()
    # def __init__(self):



    def fangfa(self):
        print self.a + self.b   # 属性 a 由父类的构造器创建，b 由子类构造器创建

    def print_b(self):
        return super(Test,self).print_a()



a = Test(123, 321)  # 我们只创建了子类的实例，而没有创建父类的实例
a.fangfa()
print a.print_b()
