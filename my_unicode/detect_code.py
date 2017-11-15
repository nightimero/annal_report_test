# -*- coding: utf-8 -*-
import chardet
with open("test.csv","rb") as f:
    data = f.read()
    print(chardet.detect(data))

# 用二进制模式读取
