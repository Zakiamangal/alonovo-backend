from __future__ import annotations
from dataclasses import dataclass


@dataclass
class DarkMoneyEntity:
    entity: str
    linked_by: str
    notes: str
