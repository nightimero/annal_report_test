# -*- coding: utf-8 -*-
# 在Python中给phantomjs设置代理
# 96  止念观息 关注
# 2016.11.15 17:13 字数 23 阅读 191评论 0喜欢 0
from selenium import webdriver
service_args = [ '--proxy=127.0.0.1:9999', '--proxy-type=socks5', ]
browser = webdriver.PhantomJS('../path_to/phantomjs',service_args=service_args)

# 利用DesiredCapabilities(代理设置)参数值，重新打开一个sessionId，我看意思就相当于浏览器清空缓存后，加上代理重新访问一次url
proxy=webdriver.Proxy()
proxy.proxy_type=ProxyType.MANUAL
proxy.http_proxy='1.9.171.51:800'
# 将代理设置添加到webdriver.DesiredCapabilities.PHANTOMJS中
proxy.add_to_capabilities(webdriver.DesiredCapabilities.PHANTOMJS)
browser.start_session(webdriver.DesiredCapabilities.PHANTOMJS)
browser.get('http://1212.ip138.com/ic.asp')
print('1: ',browser.session_id)
print('2: ',browser.page_source)
print('3: ',browser.get_cookies())

# 还原为系统代理
proxy=webdriver.Proxy()
proxy.proxy_type=ProxyType.DIRECT
proxy.add_to_capabilities(webdriver.DesiredCapabilities.PHANTOMJS)
browser.start_session(webdriver.DesiredCapabilities.PHANTOMJS)
browser.get('http://1212.ip138.com/ic.asp')
