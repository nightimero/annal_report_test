# -*- coding:utf-8 -*-
class IHateCoding(list):
    def __getslice__(self, *args):
        print 'get', args
        return super(IHateCoding, self).__getslice__(*args)

    def __setslice__(self, *args):
        print 'set', args
        super(IHateCoding, self).__setslice__(*args)

l = IHateCoding()
l.extend(xrange(5))
print l
print l[2]
l[:] = []
print l
# set (0, 2147483647, [])

a = [1, 2, 3]
print a
a[:] = []
print a
