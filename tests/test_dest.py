from citation_holdout.score import score


def test_requires_citation():
    assert score(True, citation=None) is None


def test_binds_citation():
    assert score(True, citation="x") == 1.0
