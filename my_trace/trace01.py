# -*- coding: utf-8 -*-

# python内置了一个很好的追踪模块，帮助我搞清楚发生了什么。这里有一个没什么用的python程序：

a = 1
b = 2
a = b
# 这里是对这个程序的追踪结果：

#
# (test)jhaddad@jons-mac-pro ~VIRTUAL_ENV/src$ python -m trace --trace tracing.py
#  --- modulename: tracing, funcname: <module>
# tracing.py(1): a = 1
# tracing.py(2): b = 2
# tracing.py(3): a = b
#  --- modulename: trace, funcname: _unsettrace
# trace.py(80):         sys.settrace(None)
