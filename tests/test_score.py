from citation_holdout.score import score


def test_missing_citation_is_unscored():
    assert score(True, None) is None


def test_grounded_citation_scores():
    assert score(True, "art. 5") == 1.0
    assert score(False, "art. 5") == 0.0
