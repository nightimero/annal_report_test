# -*- coding:utf-8 -*-

#todo： 获取函数名称
#在函数外部获取函数名称：

# todo:不要使用可变对象作为函数默认值  http://cenalulu.github.io/python/default-mutable-arguments/
def get_name1(a=2):
    print a+1
    pass

print dir(get_name1)
print get_name1.__name__
print get_name1.__code__.co_name
print get_name1.func_name




print get_name1.func_code.co_name

print get_name1.__code__.co_cellvars
print get_name1.__dict__


#在内部获取函数名称，第一种方法：使用sys模块
import sys
def get_name2():
    print sys._getframe().f_code.co_name

get_name2()





#第二种方法，使用装饰器


#第三种方法，使用inspect模块


#获取变量默认值
#第一种方法，在内部获取
def get_var_default(a = 1, b = 2, c = 3,args1=[1,2],kwargs1={'a':123}):
    print locals()
get_var_default()  #{'a': 1, 'c': 3, 'b': 2}





#第二种方法，在外部获取
print get_var_default.func_defaults # (1, 2, 3, [1, 2], {'a': 123})
print get_var_default.__defaults__  # (1, 2, 3, [1, 2], {'a': 123})
# print get_var_default.  #在外部获取字典，像locals()在内部一样
import inspect
print inspect.getargspec(get_var_default)
print inspect.getargspec(get_var_default).varargs
print inspect.getargspec(get_var_default).keywords
print inspect.getargspec(get_var_default).args  #['a', 'b', 'c', 'args1', 'kwargs1']
print inspect.getargspec(get_var_default).defaults # (1, 2, 3, [1, 2], {'a': 123})
print type(inspect.getargspec(get_var_default))



#在函数内部获得函数参数名称


#在方法外部获取方法名称

#在方法内部获得方法名称