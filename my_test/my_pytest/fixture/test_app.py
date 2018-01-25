# -*- coding: utf-8 -*-
import pytest


class App(object):
    a = 1
    b = 2


@pytest.fixture(scope='module')
def app():
    return App()


def test_smtp_exists(app):
    print app.a
    app.a = 3
    print app.b
    app.b = 4
    assert app.a


def test_smtp_exists2(app):
    print app.a
    print app.b
    assert app.a
