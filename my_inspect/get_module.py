# -*- coding:utf-8 -*-
from get_member import C
import inspect
# todo: http://blog.csdn.net/yugongpeng_blog/article/details/45670805
b = object()
class A: pass

print 'C in module get string:', C.__module__  # get_member
print 'C in module use inspect get instance:', \
       inspect.getmodule(C)  # C.__module__  # get_member
print type(inspect.getmodule(C))  # <type 'module'>

print 'A in module:', A.__module__  # __main__
print 'filename:', __name__   # __main__
print 'file is:', __file__

print 'get the module filename:', inspect.getfile(inspect.getmodule(C))
print 'get the module filename2:', inspect.getmodule(C).__file__

print inspect.getmoduleinfo(r'C:\Users\shawn\PycharmProjects\annal_report_test\my_inspect\get_member.pyc')

