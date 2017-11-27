# -*- coding:utf-8 -*-
from collections import namedtuple
__author__ = 'shawn'

websites = [
    ('Sohu', 'http://www.google.com/', u'张朝阳'),
    ('Sina', 'http://www.sina.com.cn/', u'王志东'),
    ('163', 'http://www.163.com/', u'丁磊')
]

Website = namedtuple('Website', ['name', 'url', 'founder'])

for website in websites:
    website = Website._make(website)
    print website
# Result:
# Website(name='Sohu', url='http://www.google.com/', founder=u'\u5f20\u671d\u9633')
# Website(name='Sina', url='http://www.sina.com.cn/', founder=u'\u738b\u5fd7\u4e1c')
# Website(name='163', url='http://www.163.com/', founder=u'\u4e01\u78ca')
