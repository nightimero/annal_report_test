# -*- coding:utf-8 -*-
from selenium import webdriver
import random
import time
import unittest

ip = "119.23.232.160:8888"
uid = random.randint(1,99999999)

class AiChat(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.get("http://" + ip + "/html/chat.html?uid=" + str(uid))

    def sendContent(self,content):
        time.sleep(0.2)
        self.driver.find_element_by_css_selector('div.chat-input-box > div > input[type="text"]').clear()
        self.driver.find_element_by_css_selector('div.chat-input-box > div > input[type="text"]').send_keys(content)
        self.driver.find_element_by_css_selector("div.chat-content-footer > div.chat-input-box > a.chat-input-send.fr").click()

    def check(self,content):
        time.sleep(1)
        result = self.driver.find_element_by_css_selector('div.chat-content-body > div:last-child').text
        assert result == content


    def test_case1(self):
        self.sendContent(u"180天")
        self.check(u'请输入正确的起购金额')

    def test_case2(self):
        self.sendContent(u"百分之五")
        self.check(u'请输入正确的起购金额')

if __name__ == '__main__':
    #unittest.main(argv=['first-arg-is-ignored'], exit=False)
    unittest.main()