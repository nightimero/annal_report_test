import time
from pywinauto.application import Application

app = Application().Start(cmd_line=u'"C:\\Program Files (x86)\\Spark\\Spark.exe"')
time.sleep(10)
sunawtframe = app.test2
sunawtframe.Wait('ready')
sunawtframe.ClickInput()
sunawtframe.ClickInput()
sunawtframe.Close()
sunawtframe2 = app.Spark
sunawtframe2.ClickInput()
sunawtframe2.MoveMouse()
sunawtframe3 = app.test2
sunawtframe3.ClickInput()

#todo:通过句柄连接已打开应用。