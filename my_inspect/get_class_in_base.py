# -*- coding:utf-8 -*-
import inspect
# base_m = __import__('base', globals(), locals(), fromlist=["*"])
base_m = __import__('base')
print 'base_m is:', base_m
# <module 'base' from 'C:\Users\shawn\PycharmProjects\annal_report_test\my_inspect\base.py'>

print inspect.getmembers(base_m, inspect.isclass)
print inspect.getmembers(base_m, inspect.isfunction)

ClassA = inspect.getmembers(base_m, inspect.isclass)[0][1]
ab = ClassA()
print ab.__class__
