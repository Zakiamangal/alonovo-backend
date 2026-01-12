from __future__ import annotations
from typing import Dict, List
import random


class OpenSecretsClient:
    """Stubbed client for lobbying + dark money mapping."""

    def get_lobbying(self, corp_name: str) -> List[Dict]:
        return self._stub_lobbying(corp_name)

    def get_dark_money_links(self, corp_name: str) -> List[Dict]:
        return self._stub_dark_money(corp_name)

    # --------------------
    # Stub data
    # --------------------

    def _stub_lobbying(self, corp_name: str) -> List[Dict]:
        issues = ["Corporate Tax", "Labor", "Supply Chain", "Trade"]
        return [
            {
                "year": y,
                "amount": random.randint(2_000_000, 10_000_000),
                "issues": random.sample(issues, 2),
            }
            for y in range(2019, 2025)
        ]

    def _stub_dark_money(self, corp_name: str) -> List[Dict]:
        return [
            {
                "entity": "Center for Retail Advocacy (501c4)",
                "linked_by": "Industry coalition membership",
                "notes": "Opaque donor structure typical of c4",
            },
            {
                "entity": "Americans for Supply Chain Efficiency (501c6)",
                "linked_by": "Trade association overlap",
                "notes": "Members undisclosed",
            },
        ]
