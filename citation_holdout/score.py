def score(grounded, citation=None):
    if citation is None:
        return None
    return 1.0 if grounded else 0.0
