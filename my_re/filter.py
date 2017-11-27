# -*- coding:utf-8 -*-
import re
string = 'abc测试123<>《》！*(^)$%~!@#$…&%￥—+=、。，；‘’“”：·`中文'
string = string.decode("utf-8")
filtrate = re.compile(u'[^\u4E00-\u9FA5]')#非中文
filtered_str = filtrate.sub(r'', string)#replace
print filtered_str
