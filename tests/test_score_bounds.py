from hypothesis import given, settings
import hypothesis.strategies as st

import stringscore.liquidmetal as lm


@given(st.text(), st.text())
@settings(max_examples=50000)
def test_score_boundaries(string, abbrev):
    score = lm.score(string, abbrev)
    assert score >= 0.0
    assert score <= 1.0
