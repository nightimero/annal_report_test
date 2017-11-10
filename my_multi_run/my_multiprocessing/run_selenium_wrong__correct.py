# -*- coding:utf-8 -*-
from selenium import webdriver
from multiprocessing import Process,freeze_support


def get_baidu():
    get_biadu_title(webdriver.PhantomJS(),'http://www.baidu.com')

def get_biadu_title(driver, url):
    # driver = getattr(webdriver, driver)()
    driver.get(url)
    print driver.title
    driver.quit()

if __name__ == "__main__":
    # run_pro = [Process(target=get_biadu_title, args=(webdriver.PhantomJS(), 'http://www.baidu.com',)) for i in range(4)]
    # 修改，就把需要传递的参数用函数封装起来就可以了。
    run_pro = [Process(target=get_baidu,) for i in range(4)]
    for t in run_pro:
        t.start()
    for t in run_pro:
        t.join()
# 为什么是顺序执行的呢？ 因为start和join(就是wait)写在了一个循环里。