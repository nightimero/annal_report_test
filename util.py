# -*- coding:utf-8 -*-

import time
from config import *
import random
import logging

logging.basicConfig(level=logging.WARNING,
                format='%(message)s',
                filename='myapp.log',
                filemode='w')

#todo: assert 后继续运行
#todo：添加到jenkins上自动执行，返回结果打印到jenkins上
#todo：打开聊天首页，图片无法加载，导致浏览器一直在加载。导致无法运行后续测试代码。

class AiDriver(object):
    def __init__(self,driver):
        self.driver = driver

    def open_page(self,page):
        self.driver.get(page)
        time.sleep(1)

    def open_chat_page(self):
        self.open_page("http://"+ip+"/html/chat.html?uid="+str(self.getuid()))

    @staticmethod
    def getuid():
        uid = str(random.randint(1,999999999))
        return uid

    def send(self,content):
        time.sleep(0.2)
        self.driver.find_element_by_css_selector('div.chat-input-box > div > input[type="text"]').clear()
        print  u'发送信息：  {}'.format(content)
        self.driver.find_element_by_css_selector('div.chat-input-box > div > input[type="text"]').send_keys(content)
        self.driver.find_element_by_css_selector("div.chat-content-footer > div.chat-input-box > a.chat-input-send.fr").click()

    def check(self,content):
        time.sleep(1)
        result = self.driver.find_element_by_css_selector('div.chat-content-body > div:last-child').text
        print u"$$$$$倒数第一个返回答案是：   {}".format(result).replace('\n','\\n')
        assert result == content

    def check2(self,content):
        result = self.driver.find_element_by_css_selector('div.chat-content-body > div:nth-last-child(2)').text
        print u"$$$$$倒数第二个返回答案是：   {}".format(result).replace('\n','\\n')
        assert result == content

    def checkin(self,content):
        time.sleep(1)
        result = self.driver.find_element_by_css_selector('div.chat-content-body > div:last-child').text
        print u"$$$$$倒数第一个在范围内的答案是：   {}".format(result)
        assert result in content

    def checkin_and_log(self,msg,content):
        time.sleep(1)
        result = self.driver.find_element_by_css_selector('div.chat-content-body > div:last-child').text
        print u"$$$$$倒数第一个在范围内的答案是：   {}".format(result)
        print u'结果为：{}'.format(result in content)
        if not result in content:
            logging.warning(msg)
    def reload_driver(self):
        self.driver.get("http://"+ip+"/html/chat.html?uid="+str(self.getuid()))