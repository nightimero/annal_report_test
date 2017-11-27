# -*- coding:utf-8 -*-
import pandas as pd

df = pd.read_csv("D:\\test1.csv", encoding='gb18030')
df.drop_duplicates()
df.dropna()
words = [u'进入咨询', u'http', u'咨询订单号', u'<span', u'草泥马', u'你妈', u'welcome', u'form submit']
for word in words:
    df.drop(df[df[u'用户输入'].str.contains(word)].index, inplace=True)

df.drop(df[df[u'用户输入'].str.match(r'[0-9]+')].index, inplace=True)
s1 = df[u'用户输入'].str.len()<=2
df.drop(s1.where(s1 == True).dropna().index, inplace=True)
df.to_csv("D:\\test2.csv", encoding='gb18030')

df_result = df.drop(df.index)
words = [u'测试', u'顾客']
for word in words:
    df_result = df_result.append(df[df[u'用户输入'].str.contains(word)])
df.to_csv("D:\\test3.csv", encoding='gb18030')


# s1 = df[u'用户输入']
# s2 = s1.str.contains(u'顾客')
# s3 = s1.drop(s2.where(s2 == True).dropna().index)
