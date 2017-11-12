# -*- coding:utf-8 -*-
import collections
__author__ = 'shawn'

fields = ['name', 'population', 'coordinates', 'capital', 'state_bird']
Town = collections.namedtuple('Town', fields)
funkytown = Town('funky', 300, 'somewhere', 'lipps', 'chicken')
print funkytown._asdict()
print funkytown.__dict__  # 也是返回的OrderedDict对象
print funkytown.__getitem__(1)

# OrderedDict([('name', 'funky'),
#              ('population', 300),
#              ('coordinates', 'somewhere'),
#              ('capital', 'lipps'),
#              ('state_bird', 'chicken')])
