# -*- coding:utf-8 -*-
from itertools import count
print 'direct use', count(10)
b = count(10)
print b.next()
print b.next()
print b.next()
print b.next()
print b.next()

# count with step
c = count(11, 3)
print c.next()
print c.next()
print c.next()
