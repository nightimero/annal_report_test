# -*- coding:utf-8 -*-
# map 和 [x for x in iterable] 的 区别
# map仅仅是做了列推导。[]做的是笛卡尔乘积。所以这里可以应用到不同的情况。
# 参考：https://my.oschina.net/zyzzy/blog/115096

def add(a,b,c):
    return a * 10000 + b * 100 + c

list1 = [11, 44, 77]
list2 = [22, 55, 88]
list3 = [33, 55, 99]

print map(add,list1,list2,list3)

print [add(x, y , z)  for x in list1 for y in list2 for z in list3]
