from __future__ import annotations
from dataclasses import dataclass, field
from typing import List, Dict


@dataclass
class PAC:
    pac_id: str
    pac_name: str
    contributions: List[Dict] = field(default_factory=list)
