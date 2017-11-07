# -*- coding:utf-8 -*-
# raise Exception(u'出错了',u'不知道什么原因')
#TODO: 打印tuple中的unicode
tuple_a = [u'出错了',u'不知道什么原因']
print tuple_a
# print [x.encode('utf-8') for x in tuple_a]
# print map(str, tuple_a)
print repr(tuple_a).decode('unicode-escape')

dict_a = {'te':u'测试',u'完全b':u'算法'}
print repr(dict_a).decode('unicode-escape')


lst = [u'\u5de5', u'\u5de5']
msg = repr(lst).decode('unicode-escape')
print msg
# [u'工', u'工']
import sys
lst = [u'\u5de5', u'\u5de5']
msg = repr([x.encode(sys.stdout.encoding) for x in lst]).decode('string-escape')
print msg
# ['工', '工']

a = u'测试'
print repr(a).decode('string-escape')  # u'\u6d4b\u8bd5'
print type(repr(a))
# todo: repr 和 str 区别