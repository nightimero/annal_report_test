# -*- coding:utf-8 -*-
# deque
# deque其实是 double-ended queue 的缩写，翻译过来就是双端队列，
# 它最大的好处就是实现了从队列 头部快速增加和取出对象: .popleft(), .appendleft() 。
#
# 你可能会说，原生的list也可以从头部添加和取出对象啊？就像这样：
#
# l.insert(0, v)
# l.pop(0)
# 但是值得注意的是，list对象的这两种用法的时间复杂度是 O(n) ，
# 也就是说随着元素数量的增加耗时呈 线性上升。而使用deque对象则是 O(1) 的复杂度，
# 所以当你的代码有这样的需求的时候， 一定要记得使用deque。
#
# 作为一个双端队列，deque还提供了一些其他的好用方法，比如 rotate 等。
#
# 举个栗子

# -*- coding: utf-8 -*-
"""
下面这个是一个有趣的例子，主要使用了deque的rotate方法来实现了一个无限循环
的加载动画
"""
import sys
import time
from collections import deque

fancy_loading = deque('>--------------------')

while True:
    print '\r%s' % ''.join(fancy_loading)
    fancy_loading.rotate(1)
    sys.stdout.flush()
    time.sleep(0.08)

# Result:

# 一个无尽循环的跑马灯
# ------------->-------

