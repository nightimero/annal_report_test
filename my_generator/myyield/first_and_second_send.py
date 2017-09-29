# -*- coding:utf-8 -*-.
# 参考： http://blog.bitfoc.us/?p=502
import time
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

# def f():
#     x = 'lo'
#     y = 'li'
#     z = yield x
#     k = yield y
#     print z + k
#     yield x
#
# g = f()
# print g.next()
# print g.send('hello')
# print g.send('test')
# print g.next()

# Traceback (most recent call last):
# lo
# li
#   File "C:/Users/shawn/PycharmProjects/annal_report_test/my_generator/myyield/muti_yield.py", line 80, in <module>
# hellotest
# lo
#     print g.next()
# StopIteration


# 第六次，next() 和 send(None) 等效
# 话说仔细看这个例子还是挺凌乱的, 因为函数f明明内部只有两个yield, 却有三次send;
# 而第一次send的实参值必须是None(否则挂), 并且最后一次send之后必然会出现一次StopIteration.
def f():
    x = 'lo'
    y = 'li'
    z = yield x
    k = yield y
    print z + k
    yield x

g = f()
print g.send(None)
print g.send('hello')
print g.send('test')
print g.send(None)



# 第七次报错和打印不同步，是随机的。所以判断协程执行抛出异常的方式特别。使用time函数确定下。
# Traceback (most recent call last):
# lo
#   File "C:/Users/shawn/PycharmProjects/annal_report_test/my_generator/myyield/first_and_second_send.py", line 107, in <module>
# li
#     print g.send(None)
# hellotest
# StopIteration
# lo

# 结果time.sleep完全没有起作用。
def f():
    x = 'lo'
    time.sleep(2)
    y = 'li'
    time.sleep(2)
    z = yield x
    time.sleep(2)
    k = yield y
    time.sleep(2)
    print z + k
    time.sleep(2)
    yield x

g = f()
print g.send(None)
print g.send('hello')
print g.send('test')
print g.send(None)

# todo： yield中time函数不起作用？ why？
