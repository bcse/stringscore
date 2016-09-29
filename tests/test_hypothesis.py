#!/usr/bin/env python
# -*- coding: utf-8 -*-

import unittest

from hypothesis import given, settings
from hypothesis import strategies

from stringscore import liquidmetal
from stringscore import quicksilver


class LiquidMetalTestCase(unittest.TestCase):

    @given(strategies.text(), strategies.text())
    @settings(max_examples=50000)
    def test_score_boundaries(self, string, abbrev):
        score = liquidmetal.score(string, abbrev)
        self.assertTrue(0.0 <= score <= 1.0)


class QuickSilverTestCase(unittest.TestCase):

    @given(strategies.text(), strategies.text())
    @settings(max_examples=50000)
    def test_score_boundaries(self, string, abbrev):
        score = quicksilver.score(string, abbrev)
        self.assertTrue(0.0 <= score <= 1.0)
