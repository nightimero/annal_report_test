# -*- coding: utf-8 -*-
# -*- coding:UTF-8 -*-
# !/user/bin/env python

import win32com.client
import time
from time import sleep

loginurl = 'http://passport.cnblogs.com/login.aspx'
loginouturl = 'http://passport.cnblogs.com/logout.aspx'
username = 'XXX'
password = 'XXX'

ie = win32com.client.Dispatch("InternetExplorer.Application")
ie.Visible = 0

ie.Navigate(loginurl)
state = ie.ReadyState
print "打开登陆页面"
time.sleep(3)
# print 'state:', ie.ReadyState
# while 1:
#     state = ie.ReadyState
#     if state == 4:
#         break
#     sleep(1)
# print "页面载入完毕，输入用户名密码"
# state = None
print ie
# todo： 代码都在报错。  这里不是sendkey，这里是赋值替代

ie.Document.getElementById("input1").value = username
ie.Document.getElementById("input2").value = password
ie.Document.getElementById("signin").click()

while 1:
    state = ie.ReadyState
    print state
    if state == 4 and str(ie.LocationURL) == "http://home.cnblogs.com/":
        break
    sleep(1)
print "登陆成功"
print '你的昵称是：'
print ie.Document.getElementById('lnk_current_user').title

# 博客园只能登录一次，注销
print '注销！'
ie.Navigate(loginouturl)
