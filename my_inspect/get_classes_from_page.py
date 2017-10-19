# -*- coding:utf-8 -*-
import os
import inspect
import pkgutil
from pprint import pprint
import page
import page.page_b
print page.__path__
print type(page.__path__)  # 尼玛，这里是list，导致后面出错。看来以后得小心啊。
print page.__name__
print type(page.__name__)
print inspect.getmembers('.page', inspect.ismodule)  # 这样不行。
print os.getcwd()+'/page'
print 'iter_modules:'
pprint([x for x in pkgutil.iter_modules(os.getcwd()+'/page')])  # 这样不行。
pprint([x for x in pkgutil.iter_modules(['C:\\Users\\shawn\\PycharmProjects\\annal_report_test\\my_inspect\\page'], 'page.')])  # 这样不行。
pprint([x for x in pkgutil.iter_modules(page.__path__, page.__name__ + ".")])
pprint([x for x in pkgutil.iter_modules(page.__path__)])
print 'walk_packages:'
# pprint([x for x in pkgutil.walk_packages(page.__path__,)])

modules_0 = [x[0] for x in pkgutil.iter_modules(page.__path__)][0]
print modules_0
print dir(modules_0)
print dir(page.page_b)


