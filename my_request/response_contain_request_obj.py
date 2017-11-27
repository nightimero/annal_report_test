# -*- coding: utf-8 -*-
# 请求与响应对象
# 任何时候进行了类似 requests.get() 的调用，你都在做两件主要的事情。
# 其一，你在构建一个 Request 对象， 该对象将被发送到某个服务器请求或查询一些资源。
# 其二，一旦 requests 得到一个从服务器返回的响应就会产生一个 Response 对象。
# 该响应对象包含服务器返回的所有信息，也包含你原来创建的 Request 对象。
# 如下是一个简单的请求，从 Wikipedia 的服务器得到一些非常重要的信息：
import requests
import json
from pprint import pprint
r = requests.get('http://en.wikipedia.org/wiki/Monty_Python')
# todo:如何漂亮的打印r.header
pprint(r.headers, indent=4)
print r.headers
pprint(str(r.headers))
print str(r.headers)
print json.dumps(str(r.headers), indent=1)

# responsse 中包含的request对象
print r.request.headers