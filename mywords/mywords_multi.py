#!/usr/bin/python
# -*- coding: utf-8 -*-
#########################################################################
# File Name: test.py
# Author: gaodengke
# mail: m18810364113_1@163.com
# Created Time: 2016-08-09 11:32:49
#########################################################################

import urllib2
import json
import pandas as pd
import multiprocessing
import threading

#todo: http://www.jianshu.com/p/afd9b3deb027
#todo: http://blog.csdn.net/onwer3/article/details/9238807
def convert(x):
    try:
        return x.astype(int)
    except:
        return x



def exam_dirty_words(df,start=0,end=10):
    for row in range(start,end):
        test_data = {"Appid": "qyzc", "Skey": "sldkjgklds",
                     "Raw_text": df[u'输入'][row],
                     "Robot_ask": ""}
        headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; rv:28.0) Gecko/20100101 Firefox/28.0'}
        body = json.dumps(test_data)

        requrl = "http://119.23.232.160:8010/api/"
        post_body = body  # urllib.urlencode(body)
        req = urllib2.Request(requrl, headers=headers, data=post_body)
        res = urllib2.urlopen(req)
        res_dict = json.loads(res.read())
        print res_dict
        df[u'实际输出'][row] =  str(res_dict["Result"]["Features"]["Abuse"])
        if df[u'实际输出'][row] != df[u'预期输出'][row]:
            print u'第%s行错误'% row
            df[u'是否错误'][row] = u'错误'
    return df

df = pd.read_csv('words.csv',encoding='gb18030',sep=',')
rows = df.shape[0]
PROCESS = 10





df = df.apply(convert)
print df.dtypes
df.to_csv('words.csv',encoding='gb18030',index=False,sep=',')

