# -*- coding: utf-8 -*-
# python C:\Python27\Scripts\pycallgraph graphviz -- prod_test\product_chat.py
# python C:\Python27\Scripts\pycallgraph -m graphviz -- prod_test\product_chat.py
# but cannot use in windows platform， NotImplementedError: The psutil module is required for non-unix platforms
# 即便装了psutil 。也报错：AttributeError: 'Process' object has no attribute 'get_memory_info'
# 参考：todo：http://mg.pov.lt/blog/hunting-python-memleaks.html
# http://pycallgraph.slowchop.com/en/master/guide/command_line_usage.html#general-arguments