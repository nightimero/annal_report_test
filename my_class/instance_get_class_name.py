# -*- coding: utf-8 -*-
# do：打印实例名称。


class Ab(object):
    def print_class_name(self):
        print self.__class__.__name__

a = Ab()
a.print_class_name()

print type(a).__name__  # 必须要是新式类，否则打印出来的是instance。

# 內建方法也可以。
print int(5).__class__.__name__
