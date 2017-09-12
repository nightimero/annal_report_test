# -*- coding:utf-8 -*-

import time
from config import *
import random

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

    def reload_driver(self):
        self.driver.get("http://"+ip+"/html/chat.html?uid="+str(self.getuid()))