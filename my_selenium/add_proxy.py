# -*- coding: utf-8 -*-
# 在Python中给phantomjs设置代理
# 96  止念观息 关注
# 2016.11.15 17:13 字数 23 阅读 191评论 0喜欢 0
 service_args = [ '--proxy=127.0.0.1:9999', '--proxy-type=socks5', ]
 browser = webdriver.PhantomJS('../path_to/phantomjs',service_args=service_args)
