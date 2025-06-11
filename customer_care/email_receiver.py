
"""Email Receiver Agent.

This agent would normally connect to Office 365 to fetch new complaint emails.
In this simplified example, it returns mock email data.
"""
from __future__ import annotations

from typing import Iterable


class EmailReceiver:
    def __init__(self, inbox_id: str):
        self.inbox_id = inbox_id

    def receive(self) -> Iterable[str]:
        """Simulate receiving raw email texts."""
        return []

    def fetch_emails(self) -> Iterable[dict]:
        """Fetch new complaint emails."""
        return [
            {
                "from": "customer@example.com",
                "subject": "Order #123 Complaint",
                "body": "OrderReference: 123\nI received a damaged product.",
            }
        ]
