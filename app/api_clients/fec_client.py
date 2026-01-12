from __future__ import annotations
from typing import List, Dict
import random


class FECClient:
    """Stubbed FEC-like client for PACs and contributions."""

    def get_corporate_pac(self, corp_name: str) -> Dict:
        return self._stub_pac(corp_name)

    def get_pac_contributions(self, pac_id: str) -> List[Dict]:
        return self._stub_pac_contributions(pac_id)

    def get_exec_personal_donations(self, exec_name: str) -> List[Dict]:
        return self._stub_exec_donations(exec_name)

    # --------------------
    # Stub data
    # --------------------

    def _stub_pac(self, corp_name: str) -> Dict:
        name_l = corp_name.lower()
        if name_l == "target corporation":
            return {"pac_name": "TargetCitizensPAC", "pac_id": "PAC-TGT-001"}
        if name_l == "walmart inc.":
            return {"pac_name": "WalmartPAC", "pac_id": "PAC-WM-001"}
        return {"pac_name": f"{corp_name} PAC", "pac_id": "PAC-GEN-999"}

    def _stub_pac_contributions(self, pac_id: str) -> List[Dict]:
        candidates = [
            ("Amy Klobuchar", "D"),
            ("Chuck Grassley", "R"),
            ("House Majority PAC (Super PAC)", "D"),
            ("Senate Leadership Fund (Super PAC)", "R"),
        ]
        return [
            {
                "recipient": name,
                "party": party,
                "amount": random.randint(10_000, 150_000),
                "cycle": 2024,
            }
            for name, party in candidates
        ]

    def _stub_exec_donations(self, exec_name: str) -> List[Dict]:
        parties = ["D", "R"]
        return [
            {
                "recipient": f"Candidate {chr(65 + i)}",
                "party": random.choice(parties),
                "amount": random.randint(250, 5000),
                "cycle": 2024,
            }
            for i in range(random.randint(1, 4))
        ]
