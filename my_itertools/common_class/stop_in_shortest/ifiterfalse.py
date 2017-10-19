# -*- coding:utf-8 -*-
from itertools import ifilterfalse
# ifilterfalse(pred, seq)
# ifilter的相反版本。
ifilterfalse(lambda x: x % 2, range(10))  # --> 0 2 4 6 8
for y in ifilterfalse(lambda x: x % 2, range(10)):
    print y
