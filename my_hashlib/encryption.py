# -*- coding:utf-8 -*-
import hashlib
__author__ = 'shawn'
print hashlib.md5('test').hexdigest()
print hashlib.sha1('test').hexdigest()


def get_file_md5(f):
    m = hashlib.md5()

    while True:
        data = f.read(10240)
        if not data:
            break

        m.update(data)
    return m.hexdigest()


with open('file_to_test_md5', 'r') as f:
    # windows 用户 要使用 'rb'方式打开文件  # 8cbd217bcb517d8ed423f7b0562968fe
    # 但是用'r'打开是可以的。
    file_md5 = get_file_md5(f)
    print file_md5

# ====update then  hashlib====
x = hashlib.md5()
x.update('hello, ')
x.update('python')
print x.hexdigest()

print hashlib.md5('hello, python').hexdigest()
