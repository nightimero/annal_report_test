# -*- coding:utf-8 -*-

# bases

# 类型对象有两个相似的成员：
# 
# base: 只读，总是返回 bases[0]。
# bases: 基类列表，可直接修改来更换基类，影响 mro 顺序。

class A(object): pass
class B(object): pass
class C(B): pass

print C.__bases__   # 直接基类型元组
# (<class '__main__.B'>,)

print C.__base__   # __bases__[0]
# <class '__main__.B'>

print C.__mro__   # mro
# (<class '__main__.C'>, <class '__main__.B'>, <type 'object'>)

C.__bases__ = (A,)  # 通过 __bases__ 修改基类

print C.__base__   # __base__ 变化
# <class '__main__.A'>

print C.__mro__   # mro 变化
# (<class '__main__.C'>, <class '__main__.A'>, <type 'object'>)
# 对多继承一样有效，比如调整基类顺序。

class C(A, B): pass

print C.__bases__
# (<class '__main__.A'>, <class '__main__.B'>)

print C.__base__
# <class '__main__.A'>

print C.__mro__
# (<class '__main__.C'>, <class '__main__.A'>, <class '__main__.B'>, <type 'object'>)

C.__bases__ = (B, A)  # 交换基类型顺序

print C.__base__   # __base__ 总是返回 __bases__[0]
# <class '__main__.B'>

print C.__mro__   # mro 顺序也发生变化
# (<class '__main__.C'>, <class '__main__.B'>, <class '__main__.A'>, <type 'object'>)
# 通过更换基类，我们可实现代码注入 (Code Inject)，影响既有类型的行为。事实上，我们还可以更改实例的类型。

class A(object): pass
class B(object): pass
a = A()
a.__class__ = B
# type(a)
# __main__.B
