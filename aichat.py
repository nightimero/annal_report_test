# -*- coding:utf-8 -*-
from case import *
from util import *
import re
from selenium import  webdriver

class AiChat(object):
    def __init__(self):
        self.driver = webdriver.Chrome()
        self.aidriver = AiDriver(self.driver)
        self.cases = Cases(self.aidriver)

    def main_test(self):
        self.aidriver.open_chat_page()
        sorted_funcs = self.get_sorted_case()
        self.run_test(sorted_funcs)

    def get_sorted_case(self):
        list_func = [func for func in Cases.__dict__.keys() if callable(getattr(Cases, func)) and re.match(r'case\d+',func)]
        sorted_funcs = sorted(list_func,key=lambda x:int(x.replace('case','')))
        return sorted_funcs

    def run_test(self,func_list):
        for i ,func in enumerate(func_list,1):
            print '\n\n\n\n===开始第{}个测试用例，名称:{}==='.format(i,func)
            getattr(self.cases,func)()

    def main_test(self):
        self.aidriver.open_chat_page()
        sorted_funcs = self.get_sorted_case()
        self.run_test(sorted_funcs)

    def suit_test(self):
        self.aidriver.open_chat_page()
        sorted_funcs = self.get_sorted_case()
        #indices = [3,4,5,9]  #第一次测试未通过用例
        # indices = [7,8]       #第二次测试未通过用例
        exclude_test= range(5,len(sorted_funcs)+1)    #停用什么类型证书节点可用用例
        test_suit = [ i for j,i in enumerate(sorted_funcs,1) if j not in exclude_test]
        self.run_test(test_suit)
#Todo: 使用进程池，运行5个进程，每个进程开始初始化，并分别执行每个测试用例。

if __name__ == '__main__':
    aichat = AiChat()
    for i in range(3):
        print u'*********开始第{}个循环************'.format(i+1)
        # aichat.main_test()
        aichat.suit_test()