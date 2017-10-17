# -*- coding:utf-8 -*-
import pandas as pd
# 导入整理后的csv文件
data = pd.read_csv(r'C:/Users/xiang.chen/Desktop/test1.csv', encoding='gbk')
# 获取加班数据
data1 = data.iloc[1::2]
# 获取姓名
col_names = data.iloc[0::2, 10]
# 将加班数据转置
data2 = data1.T
# 修改加班数据与姓名对应
data2.columns = col_names
data2.columns.name = u'姓名'
data2.index.name = u'日期'
# 处理空数据
data3 = data2.fillna('00:0000:00')
# map函数计算超过10小时的记为1，否则为0


def test(x):
    return 1 if pd.to_datetime(x[-5:]) - pd.to_datetime(x[:5]) > pd.to_timedelta(10, 'h') else 0
data4 = data3.applymap(test)
# 加班餐为中餐加晚餐
data5 = data2.count()+data4.sum()
# 导出数据
data5.to_csv('result.csv', encoding='gbk')
