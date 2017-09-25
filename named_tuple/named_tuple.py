# -*- coding:utf-8 -*-
import inspect
#todo :namedtuple 和 namedlist的用法
#http://www.jianshu.com/p/e938a06a85f4

def get_var_default(a = 1, b = 2, c = 3,args1=[1,2],kwargs1={'a':123}):
    print locals()

print type(inspect.getargspec(get_var_default))



