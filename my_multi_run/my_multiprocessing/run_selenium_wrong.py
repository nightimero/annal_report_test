# -*- coding:utf-8 -*-
from selenium import webdriver
from multiprocessing import Process,freeze_support


def get_biadu_title(driver, url):
    # driver = getattr(webdriver, driver)()
    driver.get(url)
    print driver.title
    driver.quit()

if __name__ == "__main__":
    # 在windows这样是错误的。在linux上可以跑起来。
    # 帮助文档中这样写的。
    # Ensure that all arguments to Process.__init__() are picklable. This means, in particular,
    # that bound or unbound methods cannot be used directly as the target argument on Windows —
    # just define a function and use that instead.
    # https://docs.python.org/2/library/multiprocessing.html#multiprocessing-programming

    run_pro = [Process(target=get_biadu_title, args=(webdriver.PhantomJS(), 'http://www.baidu.com',)) for i in range(4)]
    for t in run_pro:
        t.start()
    for t in run_pro:
        t.join()
# 为什么是顺序执行的呢？ 因为start和join(就是wait)写在了一个循环里。