# -*- coding: utf-8 -*-
# Gevent
#
# Gevent
# 是一个很好的库，封装了Greenlets，使得Python具备了异步调用的功能。是的，非常棒。我最爱的功能是Pool，它抽象了异步调用部分，给我们提供了可以简单使用的途径，一个异步的map()
# 函数：
from gevent import monkey

monkey.patch_all()

from time import sleep, time


def fetch_url(url):
    print "Fetching %s" % url
    sleep(10)
    print "Done fetching %s" % url


from gevent.pool import Pool

urls = ["http://baidu.com", "http://www.163.com", "http://sina.com"]

p = Pool(10)

start = time()
p.map(fetch_url, urls)
print time() - start
# 非常重要的是，需要注意这段代码顶部对gevent
# monkey进行的补丁，如果没有它的话，就不能正确的运行。如果我们让Python连续调用
# fetch_url
# 3
# 次，通常我们期望这个过程花费30秒时间。使用gevent：

# (test)
# jhaddad @ jons - mac - pro
# ~VIRTUAL_ENV / src$ python
# g.py
# Fetching
# http: // test.com
# Fetching
# http: // bacon.com
# Fetching
# http: // eggs.com
# Done
# fetching
# http: // test.com
# Done
# fetching
# http: // bacon.com
# Done
# fetching
# http: // eggs.com
# 10.001791954
# 如果你有很多数据库调用或是从远程URLs获取，这是非常有用的。我并不是很喜欢回调函数，所以这一抽象对我来说效果很好
