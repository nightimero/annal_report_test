#  -*- coding: utf-8 -*-
import win32api

# todo:练习 win32api，

#获取desktop尺寸
from win32api import GetSystemMetrics as wm

print 'width=' , wm(0)
print 'height=' , wm(1)

#获取鼠标位置
win32api.GetCursorPos() # 返回元组，横坐标和纵坐标

#移动鼠标位置
win32api.SetCursorPos((100,100))

#鼠标左键单击
import win32api
import win32con
win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP | win32con.MOUSEEVENTF_LEFTDOWN ,0,0,0,0)
win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN | win32con.MOUSEEVENTF_LEFTUP  ,0,0,0,0)#两种方法都可以，需要研究下什么情况不可以？
win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN ,0,0,0,0)  #DOWN 可以
win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP ,0,0,0,0)    #up有时不可以，看软件自己设置的事件响应
#鼠标右键单击
win32api.mouse_event(win32con.MOUSEEVENTF_RIGHTUP | win32con.MOUSEEVENTF_RIGHTDOWN, 0, 0, 0, 0)

#鼠标左键双击
win32api.mouse_event(win32con.Mouse, 0, 0, 0, 0)