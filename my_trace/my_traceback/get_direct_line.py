# -*- coding: utf-8 -*-
try:
    1/0
except Exception as e:
    print e
    print e.message


import traceback
try:
    1/0
except Exception as e:
    traceback.print_exc()

#
# traceback.print_exc()跟traceback.format_exc()有什么区别呢？
# format_exc()返回字符串，print_exc()则直接给打印出来。
# 即traceback.print_exc()与print traceback.format_exc()效果是一样的。
# print_exc()还可以接受file参数直接写入到一个文件。比如
# traceback.print_exc(file=open('tb.txt','w+'))
# 写入到tb.txt文件去。