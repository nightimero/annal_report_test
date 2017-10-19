# -*- coding:utf-8 -*-
from itertools import takewhile
# takewhile(pred, seq)
# dropwhile的相反版本。while false 就开始不take了。
takewhile(lambda x: x < 5, [1, 4, 6, 4, 1])  # --> 1 4
for y in takewhile(lambda x: x < 5, [1, 4, 6, 4, 1]):
    print y
