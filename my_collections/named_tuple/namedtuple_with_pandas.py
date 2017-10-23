# -*- coding:utf-8 -*-
from collections import namedtuple
import pandas as pd
import numpy as np
import threadpool

# Testdata = namedtuple("Testdata", ["first", "second", "third"])
# 这两种写法都可以。
Testdata = namedtuple("Testdata", "first second third")

no1 = Testdata(1, 2, 3)


def pp(data):
    print data.first
    print data.second

dates = pd.date_range('20170928', periods=6)
df = pd.DataFrame(np.random.randn(6, 4), index=dates, columns=list('ABCD'))
# print df

no2 = Testdata(df, "test", 123)
print no2
# a = [no2]
a = [no1]

pool = threadpool.ThreadPool(2)
# 这个函数就不支持namedtuple，需要字典。
# result = request.callable(*request.args, **request.kwds)
# TypeError: pp() argument after ** must be a mapping, not int
requests = threadpool.makeRequests(pp, a)
[pool.putRequest(req) for req in requests]
pool.wait()
