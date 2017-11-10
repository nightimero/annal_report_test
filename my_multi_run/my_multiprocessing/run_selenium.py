# -*- coding:utf-8 -*-
from selenium import webdriver
from multiprocessing import Process,freeze_support
# todo:使用Pool一试
# todo：使用参数一试


def get_biadu_title(driver, url):
    driver = getattr(webdriver, driver)()  # todo: 替换为Phantomjs一试
    driver.get(url)
    print driver.title
    driver.quit()

if __name__ == "__main__":
    run_pro = [Process(target=get_biadu_title, args=('PhantomJS', 'http://www.baidu.com',)) for i in range(4)]
    for t in run_pro:
        t.start()
    for t in run_pro:
        t.join()
# 为什么是顺序执行的呢？ 因为start和join(就是wait)写在了一个循环里。