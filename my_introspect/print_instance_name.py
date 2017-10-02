# -*- coding:utf-8 -*-
# todo:学习traceback模块。
import traceback

class Base(object):
    def __init__(self):
        (filename,line_number,function_name,text)=traceback.extract_stack()[-2]
        # todo: str.find 学习
        self.name = text[:text.find('=')].strip()
        self.filename = filename
        self.line_number = line_number
        self.function_name = function_name
        self.text = text

    def say_Myname(self):
        print self.name

    def say_trace(self):
        print self.filename
        print self.line_number
        print self.function_name
        print self.text

b = Base()
b.say_Myname()
b.say_trace()
a = Base()
a.say_Myname()
