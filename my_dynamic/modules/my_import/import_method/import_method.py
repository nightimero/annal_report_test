# -*- coding:utf-8 -*-
# __import__语法
# e.g：
# __import__(module_name[, globals[, locals[, fromlist]]]) #可选参数默认为globals(),locals(),[]
# __import__('os')
# __import__('os',globals(),locals(),['path','pip'])  #等价于from os import path, pip

# 用途：通常在动态加载时可以使用到这个函数，比如你希望加载某个文件夹下的所用模块，
# 但是其下的模块名称又会经常变化时，# 就可以使用这个函数动态加载所有模块了，
# 最常见的场景就是插件功能的支持。


# 第一种方式，exec
# todo： exce用法
# modules = ['module1', 'module2']
# for i in modules:
#      exec("import " + i)
#
# module1.hello1()
# module2.hello2()
#
# # 第二种方式，map __import__
#
# modules = ['module1', 'module2']
# mode = map(__import__, modules)
#
# mode[0].hello1()
# mode[1].hello2()
#
# # 第三种指定名称
#
# module1 = __import__('module1')
# anothername = __import__('module2')
#
# module1.hello1()
# # module2.hello2()
# anothername.hello2()

# 测试不使用别名  不用别名不行。
__import__('module1')
__import__('module2')

# todo：http://wsfdl.com/python/2013/11/02/Python%E6%A8%A1%E5%9D%97%E7%9A%84%E5%8A%A8%E6%80%81%E5%8A%A0%E8%BD%BD.html
# todo: __import__ 引入模块带.的存在出错的可能，比如？

module1.hello1()
module2.hello2()