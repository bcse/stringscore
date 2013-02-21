import unittest

import stringscore


class StringScoreTestCase(unittest.TestCase):

    def test_score(self):
        n = stringscore.SCORE_NO_MATCH
        m = stringscore.SCORE_MATCH
        t = stringscore.SCORE_TRAILING
        s = stringscore.SCORE_TRAILING_BUT_STARTED
        b = stringscore.SCORE_BUFFER

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
            score = round(stringscore.score(*k), 12)
            expected_score = round(sum(v) / len(v), 12)
            self.assertEqual(score, expected_score)


if __name__ == '__main__':
    unittest.main()
