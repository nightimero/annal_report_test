# -*- coding:utf-8 -*-
import re
string = "[]测试#server?user_id=110"
string = string.decode("utf-8")
filtrate = re.compile(u'[^\u4E00-\u9FA5A-Za-z0-9_]')#中文字,字母,下划线
filtered_str = filtrate.sub(r'', string)#replace
print filtered_str

