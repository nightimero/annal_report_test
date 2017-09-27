# -*- coding:utf-8 -*-
"""因为 import 不能接收变量,所以这样会提示：循环提示：No module named each"""
# modules = ['OpenSSL', 'Crypto', 'MySQLdb', 'sqlite3', 'zope.interface', 'pyasn1', 'twisted', 'django']
# for each in modules:
#     try:
#         import each
#     except Exception, e:
#         print e

"""1.动态导入模块"""

modules = ['OpenSSL', 'Crypto', 'MySQLdb', 'sqlite3', 'zope.interface', 'pyasn1', 'twisted', 'django']
for each in modules:
    try:
        __import__(each)
    except Exception, e:
        print e

"""检查模块是否导入"""
# todo: http://blog.csdn.net/csujiangyu/article/details/45285897
# todo: http://www.cnblogs.com/Xjng/p/3752681.html
import imp
print imp.find_module("sqlite3")