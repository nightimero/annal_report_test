# -*- coding: utf-8 -*-
# 裸Unicode字符
# Unicode存成六个Ascii字符怎么办？其实也可以decode

# coding=utf8
# 这是普通的Unicode
s = u'测'
for i in s: print(i)
print(repr(s))

# 这是裸Unicode，实际存成了六个Ascii
s = repr(s)[2:-1]
for i in s:  print u'单个的字符是：', i
print(repr(s))

# 转化其实也很简单
s = s.decode('unicode-escape')
for i in s: print(i)
print(repr(s))
