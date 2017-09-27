# -*- codng:utf-8 -*-
# todo: http://www.cnblogs.com/vamei/archive/2012/09/23/2698014.html
# todo: http://www.jb51.net/article/57208.htm
# https://zhidao.baidu.com/question/174797486.html
# todo: http://www.jb51.net/article/57725.htm
# http://outofmemory.cn/code-snippet/1737/python-according-process-name-shasi-process
import subprocess
rc = subprocess.call(["ls","-l"])

child = subprocess.Popen(["ping","-c","5","www.baidu.com"])
child.wait()
print("parent process")


# =====================
# stdin.write()
p = subprocess.Popen("app2.exe", stdin = subprocess.PIPE,
                     stdout = subprocess.PIPE, stderr = subprocess.PIPE, shell = False)

p.stdin.write('3/n')
p.stdin.write('4/n')
print p.stdout.read()


# #---- 结果 ----
# input x:
# input y:
# 3 + 4 = 7
# =====================
