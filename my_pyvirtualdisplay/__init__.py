# -*- coding:utf-8 -*-
# PyVirtualDisplay 0.2.1
#
# Download
# PyVirtualDisplay-0.2.1.tar.gz
# python wrapper for Xvfb, Xephyr and Xvnc
from pyvirtualdisplay import Display
from selenium import webdriver

display = Display(visible=0, size=(800, 600))
display.start()

driver = webdriver.Chrome()

# stuff ...

driver.close()
display.stop()

# 可以使使用
from xvfbwrapper import Xvfb
with Xvfb() as xvfb:
    # do stuff
    pass
