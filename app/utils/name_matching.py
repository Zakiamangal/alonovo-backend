def fuzzy_match(a: str, b: str, threshold: float = 0.7) -> bool:
    """
    Extremely simple stub. Replace with rapidfuzz / Levenshtein later.
    """
    return a.lower().split()[0] == b.lower().split()[0]
