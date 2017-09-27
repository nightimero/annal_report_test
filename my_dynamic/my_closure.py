# -*- coding:utf-8 -*-
# 获取闭包中的变量
# 参考：http://www.jianshu.com/p/3ce0d46e2b31
# 什么是闭包： 全局环境是不能向下获取到函数中的局部变量的。但是返回了一个外部函数的中内部函数
# 通过该内部函数，内部函数对内部变量有访问权，就可以访问外部函数的内部变量。
# 也就是说这个内部函数讲外部函数所包含的局部作用域打包了，从而使这个内部函数的实例，拥有一块独立
# 起来的封闭作用域，不收全局作用域，或者其他环境的影响。称之为闭包。
# 内部函数在外部函数返回后依然可以引用外部函数中的变量，称为闭包。

# 闭包函数都有一个__closure__属性，其中包含了它所引用的上层作用域的变量。

def inc():
    x = [0]  # inc 的 co_cellvars <type 'tuple'>:('x',)  inc1 的co_freevars <type 'tuple'>:('x',)
    def inner():
        x[0] += 1
        print(x[0])
    return inner
inc1 = inc()
inc2 = inc()

inc1()
inc1()
inc1()
inc2()
inc2()

# 因为函数也是对象。所以 inc1 有 __closure__属性
print type(inc1.__closure__[0])
# 在变量watch窗口中可以看到，红色的是对象，属性，列表索引，字典key等
print inc1.__closure__[0].cell_contents[0]
print inc1.__closure__[0].cell_contents.__len__
print inc1.__closure__[0].cell_contents.__len__()
# __closure__ 也可以用 func_closure 来访问。
print inc1.func_closure[0].cell_contents[0]

print inc1.func_globals