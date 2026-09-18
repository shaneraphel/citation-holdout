"""Factuality score with a citation hold-out."""

from __future__ import annotations


def score(grounded: bool, citation: str | None) -> float | None:
    if citation is None:
        return None
    return 1.0 if grounded else 0.0
