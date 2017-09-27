# -*- coding:utf-8 -*-
import os

while True:
    try:
        import xlrd
        break
    except:
        os.system('pip install xlrd')
