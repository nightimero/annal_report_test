# -*- coding:utf-8 -*-

# This is a known bug:
#
# http://bugs.python.org/issue10845
#
# Not sure if this will ever get ported to 2.7.X.
from multiprocessing import Process, freeze_support
import os
freeze_support()
# 子进程要执行的代码


def run_proc():
    pass
    # print 'Run child process %s (%s)...' % ('test', 'hhh')

# if __name__ == '__main__':
print 'Parent process %s.' % os.getpid()
p = Process(target=run_proc)
print 'Process will start.'
p.start()
p.join()
print 'Process end.'
