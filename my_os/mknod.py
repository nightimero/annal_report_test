# -*- coding: utf-8 -*-
import os

# 原因是因为windows文件系统与linux文件系统不同，没有node的概念，所以会报错。
try:
    os.mknod(r'C:\Users\shawn\Desktop\BOOKS\test\test1.txt')
except Exception as e:
    print e

# Traceback (most recent call last):
#   File "C:/Users/shawn/PycharmProjects/annal_report_test/my_os/mknod.py", line 3, in <module>
#     os.mknod('test1.txt')
# AttributeError: 'module' object has no attribute 'mknod'

# 在windows中创建文件的两种方法。 file 和 open

f = file(r'C:\Users\shawn\Desktop\BOOKS\test\test1.txt', 'w')
f.close()

with open(r'C:\Users\shawn\Desktop\BOOKS\test\test2.txt', 'w') as f:
    f.close()

f = open(r'C:\Users\shawn\Desktop\BOOKS\test\test3.txt', 'w')
f.close()