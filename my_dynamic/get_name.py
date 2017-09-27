# -*- coding:utf-8 -*-

#todo： 获取函数名称
#在函数外部获取函数名称：

# todo:不要使用可变对象作为函数默认值  http://cenalulu.github.io/python/default-mutable-arguments/
# todo：获取函数中的变量（全局，本地，闭包）
# todo：获取文件中的函数
# todo：获取模块中的函数
# todo：获取模块中的类
# todo：获取类中的方法
# todo：获取路径下的模块
def get_name1(a=2):
    print a+1
    pass

print dir(get_name1)
print get_name1.__name__
print get_name1.__code__.co_name
print get_name1.func_name
print get_name1.func_code.co_name


print get_name1.func_dict

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
def get_var_default(var1,a = 1, b = 2, c = 3,args1=[1,2],kwargs1={'a':123}):
    print locals()
get_var_default(1)  #{'a': 1, 'c': 3, 'b': 2}





#第二种方法，在外部获取
print get_var_default.func_defaults # (1, 2, 3, [1, 2], {'a': 123})
print get_var_default.__defaults__  # (1, 2, 3, [1, 2], {'a': 123})
# print get_var_default.  #在外部获取字典，像locals()在内部一样
import inspect
print inspect.getargspec(get_var_default)
print type(inspect.getargspec(get_var_default))
#namedtuple 如何取值
print inspect.getargspec(get_var_default).varargs
print inspect.getargspec(get_var_default).keywords
print inspect.getargspec(get_var_default).args  #['a', 'b', 'c', 'args1', 'kwargs1']
print inspect.getargspec(get_var_default).defaults # (1, 2, 3, [1, 2], {'a': 123})






#在函数内部获得函数参数名称


#在方法外部获取方法名称

#在方法内部获得方法名称





#获取运行是的入参。可以用来做调试。看是不是入参没有对。
def f(a, b=1, *pos, **named):
    print 'a is %s'% a

print inspect.getcallargs(f,a=2,x=4) # 并不会执行函数。
