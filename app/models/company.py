from __future__ import annotations
from dataclasses import dataclass, field
from typing import List, Optional

from app.models.officer import Officer
from app.models.pac import PAC
from app.models.lobbying import LobbyingRecord
from app.models.darkmoney import DarkMoneyEntity


@dataclass
class Company:
    name: str
    company_number: str
    jurisdiction: str
    address: str
    industry: str
    officers: List[Officer] = field(default_factory=list)
    pac: Optional[PAC] = None
    lobbying: List[LobbyingRecord] = field(default_factory=list)
    dark_money: List[DarkMoneyEntity] = field(default_factory=list)
