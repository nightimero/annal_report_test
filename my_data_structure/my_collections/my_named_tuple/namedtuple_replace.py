# -*- coding:utf-8 -*-
from collections import namedtuple
__author__ = 'shawn'

Point = namedtuple('Ponit', 'x,y')
p = Point(x=11, y=22)
# use p = p._replace instead of p._replace
p = p._replace(x=33)
print p
