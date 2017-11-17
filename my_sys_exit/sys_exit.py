# -*- coding: utf-8 -*-
#!/usr/local/bin/env python
import os, sys

# try:
#     sys.exit(0)
# except:
#     print('die')
# finally:
#     print('cleanup')

try:
    os._exit(0)
except:
    print('die')
print('os.exit')#不打印直接退出了


# 区别
#
# 综上，sys.exit()的退出比较优雅，调用后会引发SystemExit异常，可以捕获此异常做清理工作。os._exit()直接将python解释器退出，余下的语句不会执行。
#
# 一般情况下使用sys.exit()即可，一般在fork出来的子进程中使用os._exit()
#
# 一般来说os._exit() 用于在线程中退出
# sys.exit() 用于在主线程中退出。
#
# exit() 跟 C 语言等其他语言的 exit() 应该是一样的。
# os._exit() 调用 C 语言的 _exit() 函数。
#
# builtin.exit 是一个 Quitter 对象，这个对象的 call 方法会抛出一个 SystemExit 异常。

# exit(0)：无错误退出
# exit(1)：有错误退出
# 退出代码是告诉解释器的（或操作系统）

# sys.exit(n)退出方式比较优雅，它引发一个 SystemExit异常，没有捕获这个异常，会直接退出；
# 捕获这个异常可以做一些额外的清理工作。参数为n=0正常退出，n其他数值（1-127）为不正常，可抛异常事件供捕获。