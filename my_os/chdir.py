# -*- coding: utf-8 -*-
# 更换工作目录到指定目录,然后新建文件。
import os

os.chdir(r'C:\Users\shawn\Desktop\BOOKS\test')
f = file('test5.txt', 'w')
f.close()
print os.getcwd()