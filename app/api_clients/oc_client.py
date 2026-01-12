from __future__ import annotations
from typing import List, Dict


class OpenCorporatesClient:
    """Stubbed client for OpenCorporates."""

    def get_company(self, name: str) -> Dict:
        # TODO: replace with real HTTP calls to OpenCorporates
        return self._stub_company(name)

    def get_officers(self, company_number: str, jurisdiction: str) -> List[Dict]:
        # TODO: replace with real HTTP calls
        return self._stub_officers(company_number, jurisdiction)

    # --------------------
    # Stub data
    # --------------------

    def _stub_company(self, name: str) -> Dict:
        name_l = name.lower()
        if name_l in {"target", "target corporation"}:
            return {
                "name": "Target Corporation",
                "company_number": "TC-001",
                "jurisdiction": "us_mn",
                "address": "1000 Nicollet Mall, Minneapolis, MN",
                "industry": "Retail",
            }
        if name_l in {"walmart", "walmart inc.", "wal-mart"}:
            return {
                "name": "Walmart Inc.",
                "company_number": "WM-001",
                "jurisdiction": "us_ar",
                "address": "702 SW 8th Street, Bentonville, AR",
                "industry": "Retail",
            }
        return {
            "name": name,
            "company_number": "GEN-000",
            "jurisdiction": "unknown",
            "address": "unknown",
            "industry": "unknown",
        }

    def _stub_officers(self, company_number: str, jurisdiction: str) -> List[Dict]:
        if company_number == "TC-001":
            return [
                {"name": "Brian Cornell", "role": "CEO", "start": "2014-08-01"},
                {"name": "John Mulligan", "role": "COO", "start": "2015-09-01"},
            ]
        if company_number == "WM-001":
            return [
                {"name": "Doug McMillon", "role": "CEO", "start": "2014-02-01"},
                {"name": "John Furner", "role": "US CEO", "start": "2019-11-01"},
            ]
        return []
