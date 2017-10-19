# -*- coding:utf-8 -*-
# todo: http://blog.csdn.net/shuimuniao/article/details/8216683
# todo: http://www.cnblogs.com/cobbliu/archive/2012/09/04/2670178.htm
# todo: http://pyzh.readthedocs.io/en/latest/python-magic-methods-guide.html


class Foo(object):
    def __init__(self, value, filename):
        self.value = value
        self.logfile = file(filename, 'w')

    def __getstate__(self):
        """Return state values to be pickled."""
        f = self.logfile
        return self.value, f.name, f.tell()

    def __setstate__(self, state):
        """Restore state from the unpickled state values."""
        self.value, name, position = state
        f = file(name, 'w')
        f.seek(position)
        self.logfile = f

a = Foo('test', 'testfile')
