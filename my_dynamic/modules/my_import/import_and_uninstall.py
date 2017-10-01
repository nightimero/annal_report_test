# -*- coding:utf-8 -*-
# !/usr/bin/env python
import sys
__import__('a')      # 第一次导入会打印消息
del sys.modules['a']   # unimport
__import__('a')    # 再次导入还是会打印消息，因为已经unimport一次了
__import__('a')    # 这次就不会打印消息了

# todo: 导入一个文件夹下所有.py文件作为模块
# 参考： http://www.cnblogs.com/MaggieXiang/archive/2013/06/05/3118156.html
# 参考： http://xiaorui.cc/2015/09/27/python%E5%AE%9E%E7%8E%B0%E5%8A%A8%E6%80%81%E5%AF%BC%E5%85%A5%E6%A8%A1%E5%9D%97%E5%B9%B6reload%E7%B1%BB%E5%8F%8A%E5%87%BD%E6%95%B0/
# http://xbluer.github.io/note/2013/11/21/python_module/
# reload: 4. 提供类的重新加载模块不影响所提供类的任何已存实例---已存实例将继续使用原来的方法定义，只有该类的新实例使用新格式。这个原则对派生类同样适用。