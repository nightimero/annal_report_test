# -*- coding:utf-8 -*-
import collections
__author__ = 'shawn'

fields = ['name', 'population', 'coordinates', 'capital', 'state_bird']
Town = collections.namedtuple('Town', fields)
funkytown = Town('funky', 300, 'somewhere', 'lipps', 'chicken')
print funkytown._asdict()

# todo: what is orderdict
# OrderedDict([('name', 'funky'),
#              ('population', 300),
#              ('coordinates', 'somewhere'),
#              ('capital', 'lipps'),
#              ('state_bird', 'chicken')])
