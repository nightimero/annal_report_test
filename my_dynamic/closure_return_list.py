# -*- coding:utf-8 -*-
# list添加元素为append，连接两个列表为extend
# todo: 切片的函数有类似 list.slice的方法吗？
# todo: 闭包的作用是什么？
def count():
    fs =[]
    for i in range(1,4):
        def f():
            return i*i
        fs.append(f)
    return fs
f1,f2,f3 = count()
print f1()
print f2()
print f3()
# 结果是：
# 9
# 9
# 9

# 原因：
def outer():
    fs =[]
    for i in range(4):
        print "outer" ,id(i)
        inner_i = i
        def f():
            print id(inner_i), '->',inner_i
            return inner_i
        fs.append(f)
    return fs

outer1 = outer()
print [f.__closure__ for f in outer1]
print [f() for f in outer1]
