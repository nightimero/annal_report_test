# -*- coding:utf-8 -*-
from itertools import repeat

a = repeat('i am a jieba', 4)
print a.next()
print a.next()
print a.next()
print a.next()
try:
    print a.next()
except StopIteration as e:
    print e

# 因为上一个迭代器用完了。所以这里没有打印。
for x in a:
    print x

b = repeat('i am a jieba', 4)
for x in b:
    print x
