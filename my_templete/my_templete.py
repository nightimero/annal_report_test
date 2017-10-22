# -*- coding:utf-8 -*-
# !/usr/bin/env python
# -*- coding:utf-8 -*-
# 第一行：该文件在windows/Linux/Mac上均可运行
# 第二行：本模块采用标准的UTF-8编码

"""my first test module"""  # 表示模块的文档注释，任何模块代码的第一个字符串都被视为模块的文档注释

__author__ = 'Shawn'  # 使用__author__ 变量可以把作者写进去

# ★★★以上是Python模块的标准文件模版，下面才是真正的代码部分

# ★使用Python内置模块
# 第一步：导入要使用的模块，导入sys模块后，我们就有了变量sys指向该模块，
# 利用sys这个变量，就可以访问sys模块的所有功能
import sys  # 导入系统模块
import math  # 导入数学公式模块
from collections import Iterable  # 判断是否为可迭代对象
import os  # 导入os模块
import functools  # 导入functools.wraps


# 第二步：编写具体功能的函数
def test():
    args = sys.argv  # sys模块有一个argv变量，用list存储了命令行的所有参数。
    # argv至少有一个元素，因为第一个参数永远是该.py的文件名
    if len(args) == 1:
        print 'Hello, world!'
    elif len(args) == 2:
        print 'Hello, %s!' % args[1]
    else:
        print 'Too many arguments!'


if __name__ == '__main__':
    test()
    # 当我们在命令行运行hello模块文件时，Python解释器把一个特殊变量__name__ 置为__main__
    # 而如果在其他地方导入该hello模块时，if判断将失败，
    # 因此，这种if 测试可以让一个模块通过命令行运行时，执行一些额外的代码【常用于运行测试】
