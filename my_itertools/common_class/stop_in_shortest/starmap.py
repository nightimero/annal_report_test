# -*- coding:utf-8 -*-
from itertools import starmap
# starmap(func, seq)
# 将seq的每个元素以变长参数(*args)的形式调用func。
starmap(pow, [(2, 5), (3, 2), (10, 3)])  # --> 32 9 1000 121
for x in starmap(pow, [(2, 5), (3, 2), (10, 3), (11, 2)]):
    print x
