# -*- coding: utf-8 -*-
# 5）如果options很多的时候，可以进行分组，使用如下：
from optparse import OptionGroup
from optparse import OptionParser
parser = OptionParser()
group = OptionGroup(parser)

group.add_option()
parser.add_option_group(group)
