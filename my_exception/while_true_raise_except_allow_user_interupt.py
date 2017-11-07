# -*- coding:utf-8 -*-
while True:
    try:
        x = int(raw_input("please input a number:"))
        break
    except ValueError:
        print 'please input a correct Value'

print 'your input number is :{}'.format(x)

