# -*- coding:utf-8 -*-
from itertools import compress
# compress(data, selectors)
# 如果bool(selectors[n])为True，则next()返回data[n]，否则跳过data[n]。
compress('ABCDEF', [1, 0, 1, 0, 1, 1])  # --> A C E F
for x in compress('ABCDEF', [1, 0, 1, 0, 1, 1]):
    print x
