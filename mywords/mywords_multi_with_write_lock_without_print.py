#!/usr/bin/python
# -*- coding: utf-8 -*-
#########################################################################
# File Name: test.py
# Author: gaodengke
# mail: m18810364113_1@163.com
# Created Time: 2016-08-09 11:32:49
#########################################################################
import time
import urllib2
import json
import pandas as pd
import multiprocessing
import threading
import threadpool

#todo: http://www.jianshu.com/p/afd9b3deb027
#todo: http://blog.csdn.net/onwer3/article/details/9238807

start_time = time.time()
def convert(x):
    try:
        return x.astype(int)
    except:
        return x

#定义一个重试修饰器，默认重试一次
def retry(num_retries=1):
    #用来接收函数
    def decorator(func):
        #用来接收函数的参数
        def wrapper(*args,**kwargs):
            #为了方便看抛出什么错误定义一个错误变量
            last_exception =None
            #循环执行包装的函数
            for _ in range(num_retries):
                try:
                    #如果没有错误就返回包装的函数，这样跳出循环
                    return func(*args, **kwargs)
                except Exception as e:
                    #捕捉到错误不要return，不然就不会循环了
                    last_exception = e
            #如果要看抛出错误就可以抛出
            # raise last_exception
        return wrapper
    return decorator

@retry(num_retries=3)
def send_request(data,row):
    test_data = {"Appid": "qyzc", "Skey": "sldkjgklds",
                 "Raw_text": data[u'输入'][row],
                 "Robot_ask": ""}
    headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; rv:28.0) Gecko/20100101 Firefox/28.0'}
    body = json.dumps(test_data)

    requrl = "http://119.23.232.160:8010/api/"
    post_body = body  # urllib.urlencode(body)
    req = urllib2.Request(requrl, headers=headers, data=post_body)
    res = urllib2.urlopen(req)
    res_dict = json.loads(res.read())
    # print '=================res_dict is %s' % res_dict
    # print '=================Abuse is %s' % str(res_dict["Result"]["Features"]["Abuse"])
    return res_dict
def exam_dirty_words(pro_list):
    data = pro_list['df']
    # print '=================data is %s' % data
    start = int(pro_list['start'])
    end = int(pro_list['end'])
    # print '=================start is %s'% start
    # print '=================end is %s'% end
    for row in range(start,end):
        res_dict = send_request(data,row)
        lock.acquire()
        try:
            data[u'实际输出'][row] =  str(res_dict["Result"]["Features"]["Abuse"])
            if int(data[u'实际输出'][row]) != int(data[u'预期输出'][row]):
                print u'第%s行错误'% row
                data[u'结果'][row] = u'错误'
            else:
                data[u'结果'][row] = u'正确'
        finally:
            lock.release()
    # print data
    return data

df = pd.read_csv('words.csv',encoding='gb18030',sep=',')


def collect_data(request,data):
    data.to_csv('words2.csv',encoding='gb18030',index=False,sep=',')
lock = threading.Lock()
rows = df.shape[0]
PROCESS = 10
pro_list =[]
step = rows / PROCESS
for i in range(PROCESS):
    start = i * step
    if i < PROCESS - 1:
        end = (i + 1) * step
    else:
        end = (i + 1) * step + rows % step
    pro_list.append(dict(zip(('df','start','end'),(df,start,end))))
pool = threadpool.ThreadPool(PROCESS)
requests = threadpool.makeRequests(exam_dirty_words,pro_list,collect_data)
[pool.putRequest(req) for req in requests]
pool.wait()

df = df.apply(convert)
# print df.dtypes

end_time = time.time()
print '===========total_time is %s==========='%(end_time - start_time)
