# -*- coding: utf-8 -*-
import os
import stat

flags = stat.SF_NOUNLINK
path = r'C:\Users\shawn\Desktop\BOOKS\test\test1.txt'
try:
    print os.chflags(path, flags)
except Exception as e:
    print e.message
