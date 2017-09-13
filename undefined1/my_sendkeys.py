#coding: utf-8
import time
import win32com
import win32com.client

#todo: 通过win32com 来控制shell运行。通过shell运行其他window应用程序，比如：C：programfile里什么程序
shell = win32com.client.Dispatch("WScript.Shell")
shell.Run('notepad')
time.sleep(0.1)
shell.AppActivate('kladblok')
# shell.SendKeys("When Unicode characters are pasted here, errors ensue", 0)
#不行。不能成功。
shell.SendKeys(u"When Unicode characters are pasted here, harmony shall hopefully ensue".encode("gb2312"), 0)
