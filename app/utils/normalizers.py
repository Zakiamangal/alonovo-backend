def normalize_corp_name(name: str) -> str:
    return (
        name.replace("Inc.", "")
        .replace("Inc", "")
        .replace("Corporation", "")
        .replace("Corp.", "")
        .replace("Corp", "")
        .strip()
        .lower()
    )
