# -*- coding:utf-8 -*-
class Callback:
    def __init__(self, instance, function_name):
        self.instance = instance # api.self
        self.function_name = function_name # function

    def action(self, params):
        print self.instance.__getattribute__(self.function_name)
        self.instance.__getattribute__(self.function_name)(params)


class MyObj:
    def __init__(self):
        self.clb = None

    def register(self, clb):
        self.clb = clb # Callback(self, self.function.__name__)

    def do_MyObj(self):
        params = []
        self.clb.action(params)


class Api(object):
    def __init__(self, MyObj_instance):
        MyObj_instance.register(Callback(self, self.function.__name__))

    def function(self, params):
        print params
        print('function')

t = MyObj()
a = Api(t)
t.do_MyObj()
