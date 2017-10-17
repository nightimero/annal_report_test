# -*- coding:utf-8 -*-
class PersonaAiDriver(object):
    def __init__(self, driver):
        self._class = globals()[self.__class__.__name__]
        super(self._class, self).__init__(driver)


# 不建议用 self.class 代替当前类型名，因为这可能会引发混乱。

class A(object):
    def test(self):
        print "a"


class B(A):
    def test(self):     # 以 c instance 调用，那么
        super(self.__class__, self).test() # self.__class__ 就是 C 类型对象。
        print "b"     # super(C, self) 总是查找其基类 B。   # 于是死循环发生了。


class C(B):
    pass

try:
    C().test()
except RuntimeError as e:
    print e.message  # maximum recursion depth exceeded while calling a Python object