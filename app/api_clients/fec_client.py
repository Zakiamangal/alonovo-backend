from __future__ import annotations
from typing import List, Dict, Optional
import httpx

from app.core.settings import settings


class FECClient:
    BASE_URL = settings.fec_api_base_url

    def __init__(self, api_key: Optional[str] = None, timeout: float = 10.0) -> None:
        self.api_key = api_key or settings.fec_api_key
        if not self.api_key:
            raise RuntimeError("FEC_API_KEY not set")
        self.timeout = timeout


    async def get_corporate_pac(self, corp_name: str, cycle: int = 2024) -> List[Dict]:
        """
        Find committees (PACs/Super PACs) whose names or connected_organization_name
        roughly match the corporation name.
        Returns a list of committee summaries.
        """
        params = {
            "api_key": self.api_key,
            "q": corp_name,
            "cycle": cycle,
            # "sort": "total_receipts",
            # "sort_hide_null": "true",
            "per_page": 20,
        }
        url = f"{self.BASE_URL}/committees/"
        async with httpx.AsyncClient(timeout=self.timeout) as client:
            resp = await client.get(url, params=params)
            # print(resp.status_code, resp.text)  # temporary debug
            resp.raise_for_status()
            data = resp.json()
        return data.get("results", [])

    async def get_pac_contributions(self, committee_id: str, cycle: int) -> List[Dict]:
        """
        Schedule B: itemized disbursements (committee spending).
        We might also use Schedule A (incoming contributions) depending on what we want.
        Here we treat disbursements to other committees/candidates as 'contributions'.
        """
        url = f"{self.BASE_URL}/schedules/schedule_b/"
        params = {
            "api_key": self.api_key,
            "committee_id": committee_id,
            "two_year_transaction_period": cycle,
            "per_page": 100,
        }
        async with httpx.AsyncClient(timeout=self.timeout) as client:
            resp = await client.get(url, params=params)
            resp.raise_for_status()
            data = resp.json()

        results = data.get("results", [])

        # Normalize to internal structure
        contributions: List[Dict] = []
        for row in results:
            contributions.append(
                {
                    "recipient_name": row.get("recipient_name"),
                    "recipient_committee_id": row.get("recipient_committee_id"),
                    "disbursement_amount": row.get("disbursement_amount", 0.0),
                    "disbursement_date": row.get("disbursement_date"),
                    "cycle": cycle,
                }
            )
        return contributions

    async def get_exec_personal_donations(self, exec_name: str, cycle: int) -> List[Dict]:
        """
        Schedule A: individual contributions.
        This is just for sampling - real matching will need more filters.
        """
        url = f"{self.BASE_URL}/schedules/schedule_a/"
        params = {
            "api_key": self.api_key,
            "contributor_name": exec_name,
            "two_year_transaction_period": cycle,
            "per_page": 50,
        }
        async with httpx.AsyncClient(timeout=self.timeout) as client:
            resp = await client.get(url, params=params)
            print("Status:", resp.status_code)  # temporary debug
            resp.raise_for_status()
            data = resp.json()

        results = data.get("results", [])
        donations: List[Dict] = []
        for row in results:
            donations.append(
                {
                    "contributor_name": row.get("contributor_name"),
                    "contributor_employer": row.get("contributor_employer"),
                    "contributor_occupation": row.get("contributor_occupation"),
                    "recipient_name": row.get("recipient_name"),
                    "recipient_committee_id": row.get("recipient_committee_id"),
                    "contribution_receipt_amount": row.get("contribution_receipt_amount", 0.0),
                    "contribution_receipt_date": row.get("contribution_receipt_date"),
                    "cycle": cycle,
                }
            )
        return donations
