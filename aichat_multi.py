# -*- coding:utf-8 -*-
from case import *
from util import *
import re
from selenium import  webdriver
import threading


class AiChat(object):
    def __init__(self):
        self.driver = webdriver.Chrome()
        self.aidriver = AiDriver(self.driver)
        self.cases = Cases(self.aidriver)

    def main_test(self):
        self.aidriver.open_chat_page()
        sorted_funcs = self.get_sorted_case()
        self.run_test(sorted_funcs)

    @classmethod
    def get_sorted_case(cls):
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

    def run_muti_test(self,test_suit):
        self.aidriver.open_chat_page()
        print u'开始休眠10s'
        time.sleep(10)
        self.run_test(test_suit)
#Todo: 使用进程池，运行5个进程，每个进程开始初始化，并分别执行每个测试用例。

if __name__ == '__main__':
    # case_num = len(AiChat.get_sorted_case())
    case_num =3
    chat_list=[]
    thread_list = []
    #todo: 各种方法，都没有同时启动来运行。是怎么回事呢？ 尝试在run_muti_test添加休眠时间
    # for i in range(case_num):
    #     chat_list.append(AiChat())
    #     #这样传入的是函数的调用，会导致线程不会并行执行，所以需要使用args参数。
    #     # thread_list.append(threading.Thread(target=chat_list[i].run_muti_test(['case%s'%(i+1)])))
    #     # thread_list.append(threading.Thread(target=chat_list[i].run_muti_test,args=(['case%s'%(i+1)],)))
    #     #使用函数还是会这样。
    #     thread_list.append(threading.Thread(target=chat_list[i].main_test))
    #     thread_list[i].start()
    #     thread_list[i].join()

# ==========================================================
    #先new了对象也不行。
    for i in range(case_num):
        chat_list.append(AiChat())

    for i in range(case_num):
        thread_list.append(threading.Thread(target=chat_list[i].main_test))
        thread_list[i].start()
        thread_list[i].join()