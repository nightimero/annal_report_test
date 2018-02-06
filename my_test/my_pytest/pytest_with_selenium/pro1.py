# -*- coding: utf-8 -*-
def test_baidu(selenium):
    selenium.get('http://www.baidu.com')
    print selenium.title
