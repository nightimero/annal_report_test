# -*- coding:utf-8 -*-
# Series.str.replace(pat, repl, n=-1, case=True, flags=0)替换指定字符
# 参数:
# pat : 字符串,要替换的值可以是正则表达式
# repl : 字符串,替换值
# n : 整型, 要替换几处(默认-1,表示所有都要替换)
# case : 布尔值, 如果为True则是严格替换
# flags : 整型, 如果为0则没有flags
# 返回值:
# 序列Series/索引Index

import pandas as pd

df = pd.read_csv("D:\\test1.csv", encoding='gb18030')
df.drop_duplicates()
df.dropna()

s1 = df[u'用户输入'].str.replace(u'[^\u4E00-\u9FA5]','').str.len()<=3
df.drop(s1.where(s1 == True).dropna().index, inplace=True)  # 必须用== 不能用is。这里是where，不能迷信IDE
df.to_csv("D:\\test2.csv", encoding='gb18030')
