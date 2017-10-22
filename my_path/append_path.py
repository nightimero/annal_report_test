# -*- coding:utf-8 -*-
__author__ = 'shawn'
import sys
from pprint import pprint

# 默认情况下，Python解释器会搜索当前目录、所有已安装的内置模块和第三方模块，
# 搜索路径存放在sys 模块的path 变量中
pprint(sys.path)  # 上例PIL的路径：D:\python\Lib\site-packages
# 加载一个自定义模块时，Python会在指定的路径下搜索对应的.py文件，如果找不到，就会报错

sys.path.append(u'路径')  # 这种方法是在运行时修改，运行结束后失效

# 第二种方法是设置环境变量PYTHONPATH ，该环境变量的内容会被自动添加到模块搜索路径中。
# 设置方式与设置Path环境变量类似