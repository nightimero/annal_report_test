# -*- coding: utf-8 -*-
from mock import patch
from time import sleep


class Sweetness(object):
    def slow_remote_call(self):
        sleep(10)
        return "some_data"  # lets pretend we get this back from our remote api call


def test_long_call():
    s = Sweetness()
    result = s.slow_remote_call()
    assert result == "some_data"


# 当然，我们的测试需要很长的时间。
#
#
# (test)
# jhaddad @ jons - mac - pro
# ~VIRTUAL_ENV / src$ nosetests
# test_mock.py
#
# Ran
# 1
# test in 10.001
# s
#
# OK
# 太慢了！因此我们会问自己，我们在测试什么？我们需要测试远程调用是否有用，还是我们要测试当我们获得数据后要做什么？大多数情况下是后者。让我们摆脱这个愚蠢的远程调用吧：


class Sweetness(object):
    def slow_remote_call(self):
        sleep(10)
        return "some_data"  # lets pretend we get this back from our remote api call


def test_short_call():
    s = Sweetness()
    with patch.object(s, "slow_remote_call", return_value="some_data"):
        result = s.slow_remote_call()
    assert result == "some_data"
