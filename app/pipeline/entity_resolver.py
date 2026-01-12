from __future__ import annotations
from typing import List
from app.utils.name_matching import fuzzy_match


class EntityResolver:
    @staticmethod
    def match_officer_to_donations(officer_name: str, donation_records: List[dict]):
        """
        Future improvement:
        - use employer matching
        - date/cycle overlap
        """
        return [
            d
            for d in donation_records
            if fuzzy_match(officer_name, d.get("donor", officer_name))
        ]
