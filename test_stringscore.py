import unittest

from stringscore import liquidmetal
from stringscore import quicksilver


class LiquidMetalTestCase(unittest.TestCase):

    def test_score(self):
        n = liquidmetal.SCORE_NO_MATCH
        m = liquidmetal.SCORE_MATCH
        t = liquidmetal.SCORE_TRAILING
        s = liquidmetal.SCORE_TRAILING_BUT_STARTED
        b = liquidmetal.SCORE_BUFFER

        tests = {
            ('', ''): [t],
            ('', 'a'): [n],
            ('a', ''): [t],
            ('a', 'toolong'): [n],
            ('a', 'a'): [m],
            ('a', 'b'): [n],
            ('abc', ''): [t, t, t],
            ('abc', 'a'): [m, s, s],
            ('abc', 'b'): [n, m, t],
            ('abc', 'c'): [n, n, m],
            ('abc', 'd'): [n, n, n],
            ('A', 'a'): [m],
            ('A', 'b'): [n],
            ('FooBar', ''): [t, t, t, t, t, t],
            ('FooBar', 'foo'): [m, m, m, s, s, s],
            ('FooBar', 'fb'): [m, b, b, m, s, s],
            ('foobar', 'fb'): [m, n, n, m, s, s],
            ('FooBar', 'b'): [b, b, b, m, t, t],
            ('FooBar', 'ooar'): [n, m, m, n, m, m],
            ('FooBar', 'bab'): [n, n, n, n, n, n],
            ('Foo Bar', ''): [t, t, t, t, t, t, t],
            ('Foo Bar', 'foo'): [m, m, m, s, s, s, s],
            ('Foo Bar', 'fb'): [m, b, b, m, m, s, s],
            ('Foo-Bar', 'fb'): [m, b, b, m, m, s, s],
            ('Foo_Bar', 'fb'): [m, b, b, m, m, s, s],
            ('Foo Bar', 'b'): [b, b, b, m, m, t, t],
            ('Foo Bar', 'ooar'): [n, m, m, n, n, m, m],
            ('Foo Bar', 'bab'): [n, n, n, n, n, n, n],
            ('gnu\'s Not Unix', 'nu'): [b, b, b, b, b, m, m,
                                        b, b, m, m, t, t, t],
        }

        for k, v in tests.items():
            score = round(liquidmetal.score(*k), 12)
            expected_score = round(sum(v) / len(v), 12)
            self.assertEqual(score, expected_score)


class QuickSilverTestCase(unittest.TestCase):

    def test_score(self):
        tests = [
            (('', ''), 0.9),
            (('', 'a'), 0.0),
            (('a', ''), 0.9),
            (('a', 'toolong'), 0.0),
            (('a', 'a'), 1.0),
            (('a', 'b'), 0.0),
            (('abc', ''), 0.9),
            (('abc', 'a'), 0.933333333333),
            (('abc', 'b'), 0.633333333333),
            (('abc', 'c'), 0.333333333333),
            (('abc', 'd'), 0.0),
            (('A', 'a'), 1.0),
            (('A', 'b'), 0.0),
            (('FooBar', ''), 0.9),
            (('FooBar', 'foo'), 0.95),
            (('FooBar', 'fb'), 0.916666666667),
            (('foobar', 'fb'), 0.633333333333),
            (('FooBar', 'b'), 0.75),
            (('FooBar', 'ooar'), 0.666666666667),
            (('FooBar', 'bab'), 0.0),
            (('Foo Bar', ''), 0.9),
            (('Foo Bar', 'foo'), 0.942857142857),
            (('Foo Bar', 'fb'), 0.928571428571),
            (('Foo-Bar', 'fb'), 0.907142857143),
            (('Foo_Bar', 'fb'), 0.907142857143),
            (('Foo Bar', 'b'), 0.907142857143),
            (('Foo Bar', 'ooar'), 0.571428571429),
            (('Foo Bar', 'bab'), 0.0),
            (('gnu\'s Not Unix', 'nu'), 0.85),
        ]

        for k, v in tests:
            self.assertEqual(round(quicksilver.score(*k), 12), v)


if __name__ == '__main__':
    unittest.main()
