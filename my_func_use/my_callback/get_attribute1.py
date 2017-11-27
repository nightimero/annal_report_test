# -*- coding:utf-8 -*-
class C(object):
    a = 'abc'

    def __getattribute__(self, *args, **kwargs):
        print("__getattribute__() is called")
        print args
        if args[0] == 'a':
            return object.__getattribute__(self, *args, **kwargs)
        else:
            print '调用函数foo()'
            return object.__getattribute__(self, 'foo')()

    def foo(self):
        return "hello"
if __name__ == '__main__':
    c = C()
    print c.foo
