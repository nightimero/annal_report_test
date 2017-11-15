# -*- coding: utf-8 -*-
from selenium import webdriver

options = webdriver.ChromeOptions()
options.add_argument('--headless')
options.add_argument('window-size=1200x600')
options.add_argument('test-type')
options.add_argument('--no-sandbox')  # linux以root运行必须要加上。
options.add_argument('--disable-gpu')  # linux need
options.binary_location = '/opt/google/chrome/chrome'  # 必须指定到二进制文件
driver = webdriver.Chrome(chrome_options=options)
#
driver = webdriver.Chrome(chrome_options=options, executable_path='/usr/sbin/chromedriver')  # linux 需要指定
driver.get('http://www.baidu.com')
print driver.title