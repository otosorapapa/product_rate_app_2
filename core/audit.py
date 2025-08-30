"""Audit trail utilities.

For P0 this module only provides a simple in-memory log structure.
"""
from __future__ import annotations
from dataclasses import dataclass, field
from typing import List


@dataclass
class AuditLog:
    entries: List[str] = field(default_factory=list)

    def add(self, message: str) -> None:
        self.entries.append(message)

    def dump(self) -> List[str]:
        return list(self.entries)
