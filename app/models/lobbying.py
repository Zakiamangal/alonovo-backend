from __future__ import annotations
from dataclasses import dataclass
from typing import List


@dataclass
class LobbyingRecord:
    year: int
    amount: int
    issues: List[str]
