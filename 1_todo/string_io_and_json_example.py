# -*- coding: utf-8 -*-
from StringIO import StringIO
import json

io = StringIO()
json.dump(['streaming API'], io)
io.getvalue()
# '["streaming API"]'


# 2.use seperator, Compact encoding
import json

json.dumps([1, 2, 3, {'4': 5, '6': 7}], separators=(',', ':'))
'[1,2,3,{"4":5,"6":7}]'

# 3.Pretty printing:  indent参数是缩进的意思

import json

print json.dumps({'4': 5, '6': 7}, sort_keys=True,
                 indent=4, separators=(',', ': '))
# {
#     "4": 5,
#     "6": 7
# }


# 4.Decoding JSON:

import json

json.loads('["foo", {"bar":["baz", null, 1.0, 2]}]')
[u'foo', {u'bar': [u'baz', None, 1.0, 2]}]
json.loads('"\\"foo\\bar"')
u'"foo\x08ar'
from StringIO import StringIO

io = StringIO('["streaming API"]')
json.load(io)
[u'streaming API']

# 5跳过错误的键值
# 另一个比较有用的dumps参数是skipkeys，默认为False。 dumps方法存储dict对象时，key必须是str类型，如果出现了其他类型的话，
# 那么会产生TypeError异常，如果开启该参数，设为True的话，则会比较优雅的过度。


data = {'b': 789, 'c': 456, (1, 2): 123}
print json.dumps(data, skipkeys=True)
#
# {"c": 456, "b": 789}
