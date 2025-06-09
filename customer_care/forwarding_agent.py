"""Forwarding Agent."""
from __future__ import annotations

from typing import Iterable

from .data_models import ComplaintTicket


class ForwardingAgent:
    def __init__(self, recipients: Iterable[str]):
        self.recipients = list(recipients)

    def forward(self, ticket: ComplaintTicket) -> None:
        """Forward ticket details to configured recipients."""
        # In a real system this would send an email or push notification.
        for recipient in self.recipients:
            print(
                f"Forwarding ticket {ticket.case_number} to {recipient}:"
                f" {ticket.complaint_description}"
            )
