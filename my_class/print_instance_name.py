# -*- coding:utf-8 -*-
# todo:学习traceback模块。
import traceback

class Base(object):
    def __init__(self):
        (filename,line_number,function_name,text)=traceback.extract_stack()[-2]
        self.name = text[:text.find('=')].strip()
    def say_Myname(self):
        print self.name


b = Base()
b.say_Myname()
a = Base()
a.say_Myname()
