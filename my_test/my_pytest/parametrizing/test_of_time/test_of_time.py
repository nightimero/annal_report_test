# -*- coding:utf-8 -*-
import pytest
from datetime import datetime, timedelta

testdata = [
    (datetime(2001, 12, 12), datetime(2001, 12, 11), timedelta(1)),
    (datetime(2001, 12, 11), datetime(2001, 12, 12), timedelta(-1))
]


@pytest.mark.parametrize("a,b,expected", testdata)
def test_timedistance_v0(a, b, expected):
    diff = a - b
    assert diff == expected


@pytest.mark.parametrize("a,b,expected", testdata, ids=["forward", "backward"])
def test_timedistance_v1(a, b, expected):
    diff = a - b
    assert diff == expected


def idfn(val):
    if isinstance(val, (datetime,)):
        return val.strftime('%Y%m%d')
    else:
        # return "hello"+ val  # 这样是错误的。不能返回数据
        return "hello" + str(val)
        return "hello" + val


@pytest.mark.parametrize("a,b,expected", testdata, ids=idfn)
def test_timedistance_v2(a, b, expected):
    diff = a - b
    assert diff == expected

@pytest.mark.parametrize("a,b,expected", [
    pytest.param(datetime(2001, 12, 12), datetime(2001, 12, 11),
                 timedelta(1), id='forward'),
    pytest.param(datetime(2001, 12, 11), datetime(2001, 12, 12),
                 timedelta(-1), id='backward'),
])
def test_timedistance_v3(a, b, expected):
    diff = a - b
    assert diff == expected
