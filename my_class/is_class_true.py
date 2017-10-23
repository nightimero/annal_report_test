# -*- coding:utf-8 -*-
# 在 Python 中使用 bool 函数、if、while 等对某个对象进行真值判断时，有一定的算法。
#
# 以下情况则为 False
# None
# False
# 所有为 0 的数值，比如：0, 0L, 0.0, 0j
# 任何空的序列，比如： '', (), []
# 任何空的映射，比如 {}
# 用户定义的类的实例：如果该类定义了 ** __nonzero__ ** 或者 ** __len__ ** 方法，且返回值为数值 0 或者 False
# 其它所有情况都为 True
# 其实真值判断在 Python 入门时，大家都有遇到过，基本对于前 6 种会被判定为 False，大家也都清楚。
#
# 但是最后一种会被判断为 False，忽略的人可能会比较多。


class AB(object):
    def __len__(self):
        return 0


class AC(object):
    def __nonzero__(self):
        return 0

ab = AB()
if ab:
    print 'len:', 'true'
else:
    print 'len:', 'false'

ac = AC()
if ac:
    print 'nonzero:', 'true'
else:
    print 'nonzero:', 'false'
