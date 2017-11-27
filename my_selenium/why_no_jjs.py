# -*- coding: utf-8 -*-
# -*- coding: utf-8 -*-
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

cap = webdriver.DesiredCapabilities.PHANTOMJS
cap["phantomjs.page.settings.javascriptEnabled"] = True
cap["phantomjs.page.settings.resourceTimeout"] = 1000
cap["phantomjs.page.settings.loadImages"] = True
cap["phantomjs.page.settings.disk-cache"] = True
cap["phantomjs.page.settings.userAgent"] = (
"Mozilla/5.0 (Linux; Android 5.1.1; Nexus 6 Build/LYZ28E) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/48.0.2564.23 Mobile Safari/537.36"
)


# driver = webdriver.Chrome()
driver = webdriver.PhantomJS(executable_path='C:/Python27/phantomjs.exe', desired_capabilities=cap)
driver.implicitly_wait(5)
# driver = webdriver.PhantomJS()
try:
    driver.get('http://119.23.232.160:8021/index.html#/login')
    driver.implicitly_wait(10)
    time.sleep(3)
    # 以前遇到过driver.get(url)一直不返回，但也不报错的问题，这时程序会卡住，设置超时选项能解决这个问题。
    driver.set_page_load_timeout(20)
    # 设置10秒脚本超时时间
    driver.set_script_timeout(20)
    driver.maximize_window()
    time.sleep(2)
    # wait = WebDriverWait(driver, 10)
    # wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, "div.user-item > input")))
    driver.get_screenshot_as_file('test.png')
    driver.find_element_by_css_selector('div.user-item > input').clear()
    driver.find_element_by_css_selector('div.user-item > input').send_keys('17098331235')
    driver.find_element_by_css_selector('div.password-item > input').clear()
    driver.find_element_by_css_selector('div.password-item > input').send_keys('123456')
    driver.find_element_by_css_selector('div.button-item > button.login').click()
    time.sleep(3)
    assert driver.find_element_by_css_selector('div.main-bg-region > h1').text == u'欢迎进入启运智创AI数据训练平台'
finally:
    driver.quit()
    print u'退出driver'

