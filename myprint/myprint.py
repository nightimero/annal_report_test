# -*- coding: utf-8 -*-

import sys
lst = [u'\u5de5', u'\u5de5']
msg = repr([x.encode(sys.stdout.encoding) for x in lst]).decode('string-escape')
# 这是错的 msg = repr([x.encode(sys.stdout.encoding) for x in lst]).decode('unicode_escape')
msg = repr([x.encode(sys.stdout.encoding) for x in names]).decode('string-escape')
msg = repr([x.encode(sys.stdout.encoding) for x in dictb.values()[2].values()]).decode('string-escape')
#decode('unicode_escape')

#错的，tuple没有 encode ，不是str
# msg = repr([x.encode(sys.stdout.encoding) for x in dictb.items()]).decode('string-escape')
print msg
#['工', '工']

dictb ={u'msgid': u'1868108791703650108', u'localid': u'15058952180950',
       u'baseresponse': {u'errmsg': u'\u8bf7\u6c42\u6210\u529f', u'ret': 0, 'rawmsg': u'\u8bf7\u6c42\u6210\u529f'}}