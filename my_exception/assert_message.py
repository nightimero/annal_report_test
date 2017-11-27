# -*- coding:utf-8 -*-
try:
   assert 1 > 2, u'异常'
except Exception, e:
   print type(e), e.message

try:
   raise Exception(u'异常')
except Exception, e:
   pass