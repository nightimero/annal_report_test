# -*- coding: utf-8 -*-
import math

from nose.tools import assert_equal, assert_not_equal
from nose_ittr import IttrMultiplier, ittr


class TestFoo(object):
    __metaclass__ = IttrMultiplier

    def setup(self):
        if hasattr(self, 'value'):
            self.value += 3

    def teardown(self):
        pass

    @ittr(number=[1, 2, 3, 4])
    def test_even(self):
        assert_equal(self.number % 2, 0)

    @ittr(numerator=[15, 6], denominator=[2, 3])
    def test_no_remainder(self):
        assert_equal(self.numerator % self.denominator, 0)

    @ittr(value=[4, 14, 40])
    def test_prime_with_custom_setup(self):
        for i in range(3, int(math.sqrt(self.value))):
            assert_not_equal(self.value % i, 0)
