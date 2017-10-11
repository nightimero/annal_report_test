# -*- coding:utf-8 -*-
# two.py
__all__ = ['a','b'] #__为双横线
class two():
    def __init__(self):
        print('this is two')
a = 'this is two a'
b = 'this is two b'
if __name__=='__main__':
    t = two()



# one.py

# from two import *
print a
print b
t = two()

# 这时，类two() 将不会被 import * 导入进来
