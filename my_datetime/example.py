# -*- coding:utf-8 -*-
from datetime import datetime, timedelta

"""
timedelta代表两个datetime之间的时间差
"""
now = datetime.now()
past = past = datetime(2010,11,12,13,14,15,16)

timespan = now - past
#这会得到一个负数
past - now
attrs = [
("days","日"),( 'seconds',"秒"),( 'microseconds',"毫秒")
# ('min',"最小"),( 'max',"最大"),
]
for k,v in attrs:
    "timespan.%s = %s #%s" % (k,getattr(timespan, k),v)

"""
总共相差的秒数
"""
timespan.total_seconds()

"""
实例化一个timespan
请注意它的参数顺序
timedelta([days[, seconds[, microseconds[, milliseconds[, minutes[, hours[, weeks]]]]]]])
"""
timespan = timedelta(days=1)
now - timespan  # 返回的是datetime型
now + timespan

timespan * 2  # 还可以乘哦。代表二倍
timespan / 13

# 增加一个月
# todo: calendar learn
from calendar import monthrange
start = datetime.now()
now + timedelta(days=monthrange(start.year, start.month)[1])
