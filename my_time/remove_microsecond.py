# -*- coding:utf-8 -*-
import datetime
now = datetime.datetime.now()
print unicode(now.replace(microsecond=0))
# 2011-11-03 11:19:07
print type(datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S"))
print datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
