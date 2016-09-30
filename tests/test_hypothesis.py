# #!/usr/bin/env python
# # -*- coding: utf-8 -*-

# import unittest

# from hypothesis import given, settings
# from hypothesis import strategies

# from stringscore import liquidmetal
# from stringscore import quicksilver


# class LiquidMetalHypothesisTestCase(unittest.TestCase):

#     @given(strategies.text(), strategies.text())
#     @settings(max_examples=50000)
#     def test_score_boundaries(self, string, abbrev):
#         try:
#             score = liquidmetal.score(string, abbrev)
#             self.assertTrue(0.0 <= score <= 1.0)
#         except Exception as ex:
#             print('{} / {}'.format(repr(string), repr(abbrev)))
#             raise ex


# class QuickSilverHypothesisTestCase(unittest.TestCase):

#     @given(strategies.text(), strategies.text())
#     @settings(max_examples=50000)
#     def test_score_boundaries(self, string, abbrev):
#         try:
#             score = quicksilver.score(string, abbrev)
#             self.assertTrue(0.0 <= score <= 1.0)
#         except Exception as ex:
#             print('{} / {}'.format(string, abbrev))
#             raise ex


# if __name__ == '__main__':
#     unittest.main()

