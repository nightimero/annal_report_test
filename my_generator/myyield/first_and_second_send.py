# -*- coding:utf-8 -*-
def f():
    x = 'lo'
    y = 'li'
    z = (yield x) + (yield y)
    print z

# 第一次
# g = f()
# print g.next()
# print g.next()
# print g.next()  # unsupported operand type(s) for +: 'NoneType' and 'NoneType'




# 第二次 为了打印出z

# def f():
#     x = 'lo'
#     y = 'li'
#     z = (yield x) + (yield y)  # cannot concatenate 'str' and 'NoneType' objects
#     print z
#     yield x
# g = f()
# print g.next()
# print g.send('test')
# print g.next()


# 第三次 为了打印出z,多了next。原来第一个next只是进入。还没有跳过send语句的。
# 第二个send语句包含了next 和send语句。

# def f():
#     x = 'lo'
#     y = 'li'
#     yield
#     z = yield x
#     k = yield y  # cannot concatenate 'str' and 'NoneType' objects
#     print z + k
#     yield x
# g = f()
# g.next()
# g.next()
# print g.send('hello')
# print g.send('test')
# print g.next()

# 第四次 为了打印出z, 这样没有打印出来第一个x。

# def f():
#     x = 'lo'
#     y = 'li'
#     z = yield x
#     k = yield y
#     print z + k
#     yield x
#
# g = f()
# g.next()
# print g.send('hello')
# print g.send('test')
# print g.next()


# 第五次 为了打印出z, 会导致，先报错，后打印。

def f():
    x = 'lo'
    y = 'li'
    z = yield x
    k = yield y
    print z + k
    yield x

g = f()
print g.next()
print g.send('hello')
print g.send('test')
print g.next()

# Traceback (most recent call last):
# lo
# li
#   File "C:/Users/shawn/PycharmProjects/annal_report_test/my_generator/myyield/muti_yield.py", line 80, in <module>
# hellotest
# lo
#     print g.next()
# StopIteration
