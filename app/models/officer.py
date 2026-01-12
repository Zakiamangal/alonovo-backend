from __future__ import annotations
from dataclasses import dataclass, field
from typing import List, Dict


@dataclass
class Officer:
    name: str
    role: str
    start_date: str
    personal_contributions: List[Dict] = field(default_factory=list)
