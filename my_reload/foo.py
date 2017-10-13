# -*- coding:utf-8 -*-
class AA(object):
    def foo(self):
        # print "test"
        # print "test changed"
        print "test changed2"

class BB(AA):
    def foo(self):
        print "test2"
        super(BB, self).foo()
        print "test7"

# 包含super的就是不能reload
# https://stackoverflow.com/questions/32481508/autoreload-and-package-causing-typeerror-supertype-obj-obj-must-be-an-insta
