# -*- coding:utf-8 -*-
# 在多重继承初始化方法中使用 super 可能会引发一些奇怪的状况。
# 多重继承将很多问题复杂化，建议改用组合模式实现类似的功能。


class A(object):
    def __init__(self):
        print "A"
        super(A, self).__init__()  # 找到的是 B.__init__


class B(object):
    def __init__(self):
        print "B"
        super(B, self).__init__()  # object.__init__


class C(A, B):
    def __init__(self):
        A.__init__(self)
        B.__init__(self)

o = C()    # 对输出结果很意外？
# A     # super 按照 mro 列表顺序查找后续类型。
# B     # 那么在 A.__init__ 中的 super(A, self) 实际返回 B，
# B     # super(A, self).__init__() 实际是 B.__init__()。

print C.__mro__  # (<class '__main__.C'>, <class '__main__.A'>, <class '__main__.B'>, <type 'object'>)
