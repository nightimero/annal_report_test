#  -*- coding: utf-8 -*-
from util.mouse_move import *
#todo：根据句柄获取应用程序
import  win32clipboard
import win32gui
import ctypes
user32 = ctypes.windll.user32
hwnd = user32.GetForegroundWindow() #获取当前窗口句柄
hwnd = win32gui.GetForegroundWindow()
app = win32gui.GetWindowText(hwnd) #根据句柄获取应用程序名称
#获取应用尺寸
left,top,right,bottom = win32gui.GetWindowRect(hwnd)
print app

#通过类名和标题查找窗口句柄，并获得窗口位置和大小
import win32gui
import win32api

classname = 'Notepad'
titlename = u'无标题 - 记事本'

hwnd = win32gui.FindWindow(classname,titlename)
'''如果有多个相同classname和titlename的窗口，只返回一个'''
app = win32gui.GetWindowText(hwnd)

print app.decode('gb2312')  #'\xce\xde\xb1\xea\xcc\xe2 - \xbc\xc7\xca\xc2\xb1\xbe' 这样的编码是gbk编码


#todo：win32api输入中文
def input(word='test'):
    mouse_click(369,907)
    put(word)




