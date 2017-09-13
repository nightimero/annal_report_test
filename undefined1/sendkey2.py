# -*-coding:utf-8 -*-
from pywinauto.keyboard import SendKeys
#对了。通过这样的方式可以输入unicode字符
#参考：http://pywinauto.readthedocs.io/en/latest/code/pywinauto.keyboard.html
SendKeys(u'测试成功')

from pywinauto import Desktop