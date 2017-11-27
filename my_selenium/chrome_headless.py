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


# 以前遇到过driver.get(url)一直不返回，但也不报错的问题，这时程序会卡住，设置超时选项能解决这个问题。
# driver.set_page_load_timeout(20)
# 设置10秒脚本超时时间
# driver.set_script_timeout(20)