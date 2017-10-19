# -*- coding:utf-8 -*-
from itertools import ifilter
# ifilter(pred, seq)
# 内建函数filter的迭代器版本。
ifilter(lambda x: x % 2, range(10))   # --> 1 3 5 7 9
for y in ifilter(lambda x: x % 2, range(10)):
    print y
