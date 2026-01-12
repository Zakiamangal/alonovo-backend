from __future__ import annotations
from typing import Dict

from app.api_clients.oc_client import OpenCorporatesClient
from app.api_clients.fec_client import FECClient
from app.api_clients.os_client import OpenSecretsClient
from app.models.company import Company
from app.models.officer import Officer
from app.models.pac import PAC
from app.models.lobbying import LobbyingRecord
from app.models.darkmoney import DarkMoneyEntity


class InfluenceEngine:
    def __init__(self) -> None:
        self.oc = OpenCorporatesClient()
        self.fec = FECClient()
        self.os = OpenSecretsClient()

    def build_company_profile(self, name: str) -> Company:
        c = self.oc.get_company(name)
        company = Company(
            name=c["name"],
            company_number=c["company_number"],
            jurisdiction=c["jurisdiction"],
            address=c["address"],
            industry=c["industry"],
        )

        # Officers
        for o in self.oc.get_officers(company.company_number, company.jurisdiction):
            exec_dons = self.fec.get_exec_personal_donations(o["name"])
            officer = Officer(
                name=o["name"],
                role=o["role"],
                start_date=o["start"],
                personal_contributions=exec_dons,
            )
            company.officers.append(officer)

        # PAC
        pac_data = self.fec.get_corporate_pac(company.name)
        company.pac = PAC(
            pac_id=pac_data["pac_id"],
            pac_name=pac_data["pac_name"],
            contributions=self.fec.get_pac_contributions(pac_data["pac_id"]),
        )

        # Lobbying
        for l in self.os.get_lobbying(company.name):
            company.lobbying.append(LobbyingRecord(**l))

        # Dark money
        for d in self.os.get_dark_money_links(company.name):
            company.dark_money.append(DarkMoneyEntity(**d))

        return company

    def summarize(self, company: Company) -> Dict:
        pac_total = sum(x["amount"] for x in (company.pac.contributions if company.pac else []))
        lobbying_total = sum(x.amount for x in company.lobbying)
        lobbying_2024 = next((x.amount for x in company.lobbying if x.year == 2024), 0)

        score = (
            pac_total / 125_000
            + lobbying_2024 / 7_500_000
            + len(company.dark_money) * 0.5
        )

        return {
            "company": company.name,
            "industry": company.industry,
            "officers": [o.name for o in company.officers],
            "pac_total": pac_total,
            "lobbying_total": lobbying_total,
            "lobbying_2024": lobbying_2024,
            "dark_money_links": len(company.dark_money),
            "influence_score": round(score, 2),
        }
