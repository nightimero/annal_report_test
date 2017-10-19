# -*- coding:utf-8 -*-
from itertools import chain

# chain(p, q, ...)
# 迭代至序列p的最后一个元素后，从q的第一个元素开始，直到所有序列终止。
chain('ABC', 'DEF')  # --> A B C D E F
for x in chain('ABC', 'DEF'):
    print x
