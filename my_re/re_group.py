# -*- coding:utf-8 -*-
import re

times = []
messages = re.compile(r'(?P<time>..:..:.. ..).*?<b>(?P<usrname>.*?):</b>').finditer(search)

for result in messages:
    times.append(result.group('time'))

for result in messages:
    times.append(result.group('time'))
# You can say this though:
times = [result.group('time') for result in messages]
