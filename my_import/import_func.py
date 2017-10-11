# -*- coding:utf-8 -*-
import imp
import os
import sys
# module_a = __import__("my_high_order_func.test_module_b")

# ===========================
# 下面是可以的。
# module_a = __import__("my_high_order_func", globals(), locals(), ["test_module_b"])
# module_a = __import__("my_high_order_func", ["test_module_b"])
# b = module_a.test_module_b.B()
# b.print_b()
#  不可以错误的写法。__import__函数如果有list参数，必须要有global和locals
# ===========================
module_a = __import__("my_high_order_func.test_module_b") # 这样也可以。
b = module_a.test_module_b.B()
b.print_b()
# 这样导入了。是预期之外的。
# 'my_high_order_func': <module 'my_high_order_func' from 'C:\Users\shawn\PycharmProjects\annal_report_test\my_high_order_func\__init__.pyc
# ============================
# print os.path.dirname(os.getcwd())+"/my_high_order_func"
# module_a = imp.load_module("test_module_b",*imp.find_module("test_module_b",[os.path.dirname(os.getcwd())+"/my_high_order_func"]))
# b = module_a.B()  # 注意和__import__的区别。
# b.print_b()
#  通过打印modules可以看出 test_module_b': <module 'test_module_b' from
# 'C:\Users\shawn\PycharmProjects\annal_report_test/my_high_order_func\test_module_b.pyc
# 这样最好。只导入了需要的模块。没有导入
# ============================
print sys.path
print dir(module_a)
print sys.modules
