# -*- coding:utf-8 -*-

# 从另外一个文件中引入一个类，也会触发另一个文件中普通代码运行的。
# 但是触发完成后，不会引入普通的类或者函数。
from my_import_b import Bb,pp1
print 'test'
pp1()