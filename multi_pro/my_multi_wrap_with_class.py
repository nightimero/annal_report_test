# -*-coding:utf-8 -*-
import random
import threading
import time


#todo: 用多线程运行类中的方法。

#todo： 用多线程运行函数。
class my_thread():
    def thread_run(urls):
        print 'Current %s is  running...' % threading.currentThread().name
        for url in urls:
            print "%s ---->>> %s" %(threading.currentThread().name,url)
            time.sleep(random.random())
        print "%s ended."  % threading.currentThread().name

print '%s is running ...' % threading.currentThread().name

a = my_thread()
b = my_thread()
#todo: 为什么这里报错，但是奇怪的是，在aichat里面没有报错。
t1 = threading.Thread(target=a.thread_run,name='Thread_1',args=(['url_1','url_2','url_3'],))
t2 = threading.Thread(target=b.thread_run,name='Thread_2',args=(['url_4',"url_5",'url_6'],))

t2.start()
t1.join()
t2.join()
print '%s ended '% threading.currentThread().name
