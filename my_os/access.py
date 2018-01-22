# -*- coding: utf-8 -*-
import os

print os.access(r'C:\Users\shawn\Desktop\BOOKS\test\test1.txt', os.F_OK)  # 文件是否存在
print os.access(r'C:\Users\shawn\Desktop\BOOKS\test\test1.txt', os.R_OK)  # 文件是否可读
print os.access(r'C:\Users\shawn\Desktop\BOOKS\test\test1.txt', os.W_OK)  # 文件是否可写
print os.access(r'C:\Users\shawn\Desktop\BOOKS\test\test1.txt', os.X_OK)  # 文件是否可执行
