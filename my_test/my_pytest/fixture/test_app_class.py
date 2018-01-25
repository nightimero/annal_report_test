# -*- coding: utf-8 -*-
import pytest


class App(object):
    a = 1
    b = 2


@pytest.fixture(scope='module')
def app():
    return App()


class TestSMTP(object):
    @pytest.mark.parametrize('num', [1, 2])
    def test_smtp_exists(self, num, app):
        print app.a
        app.a = 3
        print app.b
        app.b = 4
        assert app.a
        print 'num is:', num

    def test_smtp_exists2(self, app):
        print app.a
        print app.b
        assert app.a
