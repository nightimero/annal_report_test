# -*- coding: utf-8 -*-

# 准备的请求 （Prepared Request）
# 当你从 API 或者会话调用中收到一个 Response 对象时，request 属性其实是使用了 PreparedRequest。
# 有时在发送请求之前，你需要对 body 或者 header （或者别的什么东西）做一些额外处理，下面演示了一个简单的做法：

from requests import Request, Session

url = ''
data = ''
header = ''
stream = ''
verify = ''
proxies = ''
cert = ''
timeout = ''

s = Session()
req = Request('GET', url,
              data=data,
              headers=header
              )
prepped = req.prepare()

# do something with prepped.body
# do something with prepped.headers

resp = s.send(prepped,
              stream=stream,
              verify=verify,
              proxies=proxies,
              cert=cert,
              timeout=timeout
              )

print(resp.status_code)
# 由于你没有对 Request 对象做什么特殊事情，你立即准备和修改了 PreparedRequest 对象，然后把它和别的参数一起发送到 requests.* 或者 Session.*。
#
# 然而，上述代码会失去 Requests Session 对象的一些优势， 尤其 Session 级别的状态，例如 cookie 就不会被应用到你的请求上去。
# 要获取一个带有状态的 PreparedRequest， 请用 Session.prepare_request() 取代 Request.prepare() 的调用，如下所示：

from requests import Request, Session

s = Session()
req = Request('GET', url,
              data=data,
              headers=header
              )

prepped = s.prepare_request(req)

# do something with prepped.body
# do something with prepped.headers

resp = s.send(prepped,
              stream=stream,
              verify=verify,
              proxies=proxies,
              cert=cert,
              timeout=timeout
              )

print(resp.status_code)
