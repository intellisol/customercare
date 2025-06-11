
"""Forward tickets to internal recipients."""

from __future__ import annotations

from typing import Iterable

from .config import Config
from .data_extraction import TicketData
from .data_models import ComplaintTicket


FORWARD_TEMPLATE = (
    "Forwarding ticket {case} for order {order} from {email}:\n{complaint}"
)


def format_forward(ticket: TicketData, case_number: int) -> str:
    return FORWARD_TEMPLATE.format(
        case=case_number,
        order=ticket.order_reference,
        email=ticket.customer_email,
        complaint=ticket.complaint_description,
    )


def recipients(config: Config) -> list:
    return config.recipients


class ForwardingAgent:
    def __init__(self, recipients: Iterable[str]):
        self.recipients = list(recipients)

    def forward(self, ticket: ComplaintTicket) -> None:
        """Forward ticket details to configured recipients."""
        for recipient in self.recipients:
            print(
                f"Forwarding ticket {ticket.case_number} to {recipient}: {ticket.complaint_description}"
            )

