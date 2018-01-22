# -*- coding: utf-8 -*-
import datetime
print datetime.date.today()
today = datetime.date.today()
birthday = today - datetime.timedelta(days=10*366)
print birthday

# todo： https://codeday.me/bug/20170621/27799.html 2018-1-22 非标准库获得闰年前方案。