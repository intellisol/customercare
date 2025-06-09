"""Placeholder email receiver."""

from typing import Iterable


class EmailReceiver:
    def __init__(self, inbox_id: str):
        self.inbox_id = inbox_id

    def receive(self) -> Iterable[str]:
        """Simulate receiving raw email texts."""
        # Placeholder implementation
        return []
