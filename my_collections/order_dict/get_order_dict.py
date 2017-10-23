# -*- coding:utf-8 -*-
from collections import OrderedDict
__author__ = 'shawn'

# 在Python中，dict这个数据结构由于hash的特性，是无序的，
# 这在有的时候会给我们带来一些麻烦， 幸运的是，collections模块为我们提供了OrderedDict，
# 当你要获得一个有序的字典对象时，用它就对了。

# [] 和 () list 和tuple 可以混用。
items = [
    ['A', 1],
    ('B', 2),
    ('C', 3)
]

items = (
    ('A', 1),
    ('B', 2),
    ('C', 3)
)

regular_dict = dict(items)
ordered_dict = OrderedDict(items)

print 'Regular Dict:'
for k, v in regular_dict.items():
    print k, v

print 'Ordered Dict:'
for k, v in ordered_dict.items():
    print k, v


# Result:
# Regular Dict:
# A 1
# C 3
# B 2
# Ordered Dict:
# A 1
# B 2
# C 3

