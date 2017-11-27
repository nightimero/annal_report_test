# -*- coding:utf-8 -*-
# raise Exception(u'发送消息错误', u'发送的消息')
import sys


class CheckError(Exception):
    def __init__(self, *args):
        self.value = args

    def __str__(self):
        print u'异常信息：', repr([x.encode(sys.stdout.encoding) for x in self.value]).decode('string-escape')
        return repr([x.encode(sys.stdout.encoding) for x in self.value]).decode('string-escape')


raise CheckError(u'在fasdf',u'测试')
