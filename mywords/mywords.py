#!/usr/bin/python
# -*- coding: utf-8 -*-
#########################################################################
# File Name: test.py
# Author: gaodengke
# mail: m18810364113_1@163.com
# Created Time: 2016-08-09 11:32:49
#########################################################################
import time
import urllib
import urllib2
import json
import pandas as pd
import sys

# with open('words.csv','rb') as f:
#     reader = csv.DictReader(f)
#     # reader = csv.reader(f)
#     row_dict =[]
#     for row in reader:
#         #todo: list 不能decode
#         print row
#         # try: print [x.decode('gb18030') for x in row] ;result: [u'\u8f93\u5165', u'\u9884\u671f\u8f93\u51fa', u'\u5b9e\u9645\u8f93\u51fa']
#         row_dict.append(json.dumps(row,encoding='gb18030',ensure_ascii=False))
#         # print json.dumps([x.decode('gb18030') for x in row],ensure_ascii=False)

# with open('words1.csv','w') as f:
#     writer = csv.DictWriter(f, sorted(d[0].keys()))
#     # try: csv 模块在输出writheheader的时候有编码问题 ; result:所以不使用它。
#     writer.writeheader()
#     for line in d:
#         writer.writerow(line,)

def convert(x):
    try:
        return x.astype(int)
    except:
        return x

df = pd.read_csv('words.csv',encoding='gb18030',sep=',')

rows = df.shape[0]
for row in range(int(rows)):
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
df = df.apply(convert)
print df.dtypes
df.to_csv('words.csv',encoding='gb18030',index=False,sep=',')

