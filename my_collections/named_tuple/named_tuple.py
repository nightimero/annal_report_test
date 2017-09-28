# -*- coding:utf-8 -*-
import inspect
# task :namedtuple 和 namedlist的用法 result：没有类似的namedlist ，需要自己实现。
# http://www.jianshu.com/p/e938a06a85f4
# https://stackoverflow.com/questions/2970608/what-are-named-tuples-in-python
# 这篇文章详细回答了named tuple的用处。相对于字典，更简单的访问，想类型属性一样，用一个.就可以了。
# 也可以像普通的tuple一样，使用索引访问。但是不能设置值，和普通的tuple一样。
# 没有类似namedtuple的namedlist，需要自己实现。还不如用字典。
def get_var_default(a = 1, b = 2, c = 3,args1=[1,2],kwargs1={'a':123}):
    print locals()

print type(inspect.getargspec(get_var_default))



