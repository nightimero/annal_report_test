# -*- coding: utf-8 -*-
import pytest


@pytest.fixture()
def before():
    print 'before test'
    return "abc"


def test1(before):
    print before
    print 'func test1'


def test2(before):
    print 'func test2'


if __name__ == "__main__":
    pytest.main("fixture.py -s -v")
