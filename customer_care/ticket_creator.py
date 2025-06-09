"""Ticket Creation Agent."""
from __future__ import annotations

from datetime import datetime
from typing import Optional

from .data_models import ComplaintTicket


def _current_time() -> datetime:
    return datetime.utcnow()


class TicketCreator:
    def create_ticket(
        self, customer_email: str, order_reference: str, complaint_description: str
    ) -> ComplaintTicket:
        """Create a complaint ticket and return the dataclass."""
        ticket = ComplaintTicket(
            customer_email=customer_email,
            order_reference=order_reference,
            complaint_description=complaint_description,
            complaint_datetime=_current_time(),
        )
        return ticket
