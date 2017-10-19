# -*- coding:utf-8 -*-
from itertools import imap
# imap(func, p, q, ...)
# 内建函数map的迭代器版本。
imap(pow, (2, 3, 10), (5, 2, 3))  # --> 32 9 1000
for y in imap(pow, (2, 3, 10), (5, 2, 3)):
    print y
print [x for x in imap(pow, (2, 3, 10), (5, 2, 3))]
print map(pow, (2, 3, 10), (5, 2, 3))
