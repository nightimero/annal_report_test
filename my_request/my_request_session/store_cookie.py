# -*- coding: utf-8 -*-
# 1.会话对象

# 在以上的请求中，每次请求其实都相当于发起了一个新的请求。也就是相当于我们每个请求都用了不同的浏览器单独打开的效果。
# 也就是它并不是指的一个会话，即使请求的是同一个网址。比如

import requests

requests.get('http://httpbin.org/cookies/set/sessioncookie/123456789')
r = requests.get("http://httpbin.org/cookies")
print(r.text)
# 结果是

# {
#     "cookies": {}
# }

# 1.1 use request.session can storage the session
# 很明显，这不在一个会话中，无法获取
# cookies，那么在一些站点中，我们需要保持一个持久的会话怎么办呢？就像用一个浏览器逛淘宝一样，在不同的选项卡之间跳转，这样其实就是建立了一个长久会话。
#
# 解决方案如下

import requests

s = requests.Session()
s.get('http://httpbin.org/cookies/set/sessioncookie/123456789')
r = s.get("http://httpbin.org/cookies")
print(r.text)
# 在这里我们请求了两次，一次是设置
# cookies，一次是获得
# cookies
#
# 运行结果
#
# {
#     "cookies": {
#         "sessioncookie": "123456789"
#     }
