# -*- coding: utf-8 -*-
import pytest


class TestParam(object):
    @pytest.mark.parametrize("x, y", [
        (1, 2),
        (3, 4),
    ])
    def test_x(self, x, y):
        assert x + y == 3


@pytest.mark.parametrize("x, y", [
    (1, 2),
    (3, 4),
])
def test_x(x, y):
    assert x + y == 3


@pytest.mark.parametrize("x", [1, 2])
@pytest.mark.parametrize("y", [1, 2])
def test_y(x, y):
    assert x + y == 3
