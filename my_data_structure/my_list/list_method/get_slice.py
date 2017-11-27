# -*- coding:utf-8 -*-
import sys


class IHateCoding(list):
    def __getslice__(self, *args):
        print 'get:', args
        return super(IHateCoding, self).__getslice__(*args)

    def __setslice__(self, *args):
        print 'set:', args
        super(IHateCoding, self).__setslice__(*args)

l = IHateCoding()
l.extend(xrange(5))
print l[-1]
print l[-2:-1]  # get: (3, 4)
print l[:]  # get: (0, 9223372036854775807L)
l[:] = []  # set: (0, 9223372036854775807L, [])
l[: -1] = []
print l
print sys.maxsize  # 9223372036854775807
# set (0, 2147483647, [])
