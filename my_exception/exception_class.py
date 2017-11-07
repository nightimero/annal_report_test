# -*- coding:utf-8 -*-
class MyException(Exception):
    def __init__(self, value):
        self.value = value * value

    def __str__(self):
        return self.value

try:
    raise MyException(3)
except MyException as e:
    print e.value
