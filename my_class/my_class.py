# -*- coding: utf-8 -*- 
class Abc(object):
    def __init__(self, name):
        self.name = name

    def __repr__(self):
        return "Abc(name=%s)" % self.name

    # 没有__str__就会返回__repr__
    def __str__(self):
        return "str %s" % self.name

print type(Abc('tester'))
print Abc('tester')

class AA(object):
    def __init__(self):
        print self.__class__.__name__

aa = AA()