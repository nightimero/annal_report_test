# -*- coding:utf-8 -*-
for line in open("myword"):
    for word in line.split():
        if word.endswith('is'):
            print word