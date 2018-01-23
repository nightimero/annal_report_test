# -*- coding: utf-8 -*-
import pytest


@pytest.fixture()
def before():
    print 'before test'
    return "abc"


# def test1(before()): 这样是错误的。
def test1(before):
    print 'func test1'


def test2():
    # before 这样不行
    before()
    print 'func test2'

# 两种方法使用fixture。
# 一、在函数或方法开始加注解。
# 二、在函数或方法内部调用。
class Testhaha(object):
    # @pytest.mark.usefixtures("before")
    def test3(self):
        print before()
        print 'func test3'

    def test4(self):
        print 'func test4'


if __name__ == "__main__":
    pytest.main("fixture.py -s -v")
