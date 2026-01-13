import asyncio
from app.api_clients.fec_client import FECClient
from app.core.settings import settings


async def main() -> None:
    fec = FECClient()
    exec_name = settings.fec_executive_name

    donations = await fec.get_exec_personal_donations(exec_name, cycle=2024)
    print(f"Found {len(donations)} donations for:", exec_name)
    for d in donations[:10]:
        print(
            d["contribution_receipt_date"],
            d["contribution_receipt_amount"],
            "->",
            d["recipient_name"],
            "| employer:", d["contributor_employer"],
        )


if __name__ == "__main__":
    asyncio.run(main())
