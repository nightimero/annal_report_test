# -*- coding:utf-8 -*-

# 第一个功能 根据匹配删除
test1 = "say hello world yas"

print test1.strip("say")

print test1.strip("say").strip()

print "".join(test1.split(" "))  # sayhelloworldyas

# rsplit 是什么？

print "lstrip", test1.lstrip("say")
print "rstrip", test1.rstrip("say")

# 第二个功能，根据匹配分隔。

a="alvy.test.txt"

print a.split(".")
print a.split(".", 1)  # 根据前一个分隔符分隔
print a.split(".", 2)  # 根据前两个个分隔符分隔

# 没有 lsprint这个函数。 split就相当于lsplit

print "rsplit,sep:", a.rsplit(".", 1)  # 根据从右开始前一个分隔符分隔
print "rsplit,sep:", a.rsplit(".", 2)  # 根据从右开始前两个个分隔符分隔



#
# 应用：
# 我们可以利用rsplit('.',1)来判断文件类型
# 比如我们需要txt,pdf文件
# ALLOWED_EXTENSION=['txt','pdf']
# def allowed_file(filename):
#     return '.' in filename and filename.rsplit('.',1)[1] in ALLOWED_EXTENSION


