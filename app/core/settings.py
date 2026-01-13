import os
from dataclasses import dataclass

from dotenv import load_dotenv

DEBUG = os.getenv("DEBUG", "True").lower() == "true"

load_dotenv(".env.dev" if DEBUG else ".env.prod")


@dataclass
class Settings:
    debug: bool = True
    port: int = 8000
    postgres_username: str = "postgres"
    postgres_password: str = "postgres"
    postgres_host: str = "db"
    postgres_port: int = 5432
    postgres_db: str = "alonovo_db"

    fec_api_base_url: str = None
    fec_api_key: str = None
    fec_executive_name: str = None
    fec_corporate_name: str = None

    def __post_init__(self):
        self.debug = os.getenv("DEBUG", "True").lower() == "true"
        self.port = int(os.getenv("PORT", "8000"))

        required = [
            "POSTGRES_USERNAME",
            "POSTGRES_PASSWORD",
            "POSTGRES_HOST",
            "POSTGRES_PORT",
            "POSTGRES_DB",
            "FEC_API_BASE_URL",
            "FEC_API_KEY",
            "FEC_EXECUTIVE_NAME",
            "FEC_CORPORATE_NAME",
        ]

        for var in required:
            value = os.getenv(var)
            if not value:
                raise ValueError(f"Missing required environment variable: {var}")
            if var == "POSTGRES_PORT":
                setattr(self, var.lower(), int(value))
            else:
                setattr(self, var.lower(), value)

    def get_db_url(self):
        return f"postgresql+psycopg2://{self.postgres_username}:{self.postgres_password}@{self.postgres_host}:{self.postgres_port}/{self.postgres_db}"


settings = Settings()
