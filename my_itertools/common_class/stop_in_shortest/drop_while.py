# -*- coding:utf-8 -*-
from itertools import dropwhile
# dropwhile(pred, seq)
# 当pred对seq[n]的调用返回False时才开始迭代。
# why,at last thers is a 1. while是开始，开始之后就不判断了。
# 一旦开始为真，就不drop了。
dropwhile(lambda y: y < 5, [1, 4, 6, 4, 1])  # --> 6 4 1
for x in dropwhile(lambda y: y < 5, [1, 4, 6, 4, 1]):
    print x
for x in dropwhile(lambda y: y < 5, [1, 4, 6, 4, 1, 4, 2]):
    print x
