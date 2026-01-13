import asyncio
from app.api_clients.fec_client import FECClient
from app.core.settings import settings

async def main() -> None:
    fec = FECClient()
    corp_name = settings.fec_corporate_name

    committees = await fec.get_corporate_pac(corp_name, cycle=2024)
    print("FEC committees for:", corp_name)
    for c in committees[:5]:
        print(
            c.get("committee_id"),
            c.get("name"),
            c.get("committee_type_full"),
            c.get("connected_organization_name"),
            sep="\n"
        )

    if committees:
        committee_id = committees[0]["committee_id"]
        contributions = await fec.get_pac_contributions(committee_id, cycle=2024)
        print("\nSample contributions for", committee_id)
        for row in contributions[:5]:
            print(row)

if __name__ == "__main__":
    asyncio.run(main())
