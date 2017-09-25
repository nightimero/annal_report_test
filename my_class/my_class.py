# -*- coding: utf-8 -*- 
class Abc(object):
    def __init__(self,name):
        self.name = name
    def __repr__(self):
        return "Abc(name=%s)"%self.name

print type(Abc('tester'))
print Abc('tester')