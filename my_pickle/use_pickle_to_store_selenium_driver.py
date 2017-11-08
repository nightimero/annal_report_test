# -*- coding:utf-8 -*-
from selenium import webdriver
import cPickle as pickle
driver = webdriver.PhantomJS()
pickle.dump(driver, open("tmp.txt", "w"))
#  Cannot pickle <type '_subprocess_handle'> objects

# 可以被序列化的类型有：
# * None,True 和 False;
# * 整数，浮点数，复数;
# * 字符串，字节流，字节数组;
# * 包含可pickle对象的tuples，lists，sets和dictionaries；
# * 定义在module顶层的函数：
# * 定义在module顶层的内置函数；
# * 定义在module顶层的类；
# * 拥有__dict__()或__setstate__()的自定义类型；
# 注意：对于函数或类的序列化是以名字来识别的，所以需要import相应的module。

# http://m.jb51.net/article/57661.htm
