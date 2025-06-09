"""Simple data extraction from email text."""

import re
from dataclasses import dataclass


@dataclass
class TicketData:
    customer_email: str
    order_reference: str
    complaint_description: str


EMAIL_RE = re.compile(r"Email:\s*(?P<email>.+)")
ORDER_RE = re.compile(r"Order:\s*(?P<order>.+)")
COMPLAINT_RE = re.compile(r"Complaint:\s*(?P<complaint>.+)", re.DOTALL)


def extract(email_text: str) -> TicketData | None:
    """Extract ticket fields from the given email text."""
    email_match = EMAIL_RE.search(email_text)
    order_match = ORDER_RE.search(email_text)
    complaint_match = COMPLAINT_RE.search(email_text)

    if not (email_match and order_match and complaint_match):
        return None

    return TicketData(
        customer_email=email_match.group("email").strip(),
        order_reference=order_match.group("order").strip(),
        complaint_description=complaint_match.group("complaint").strip(),
    )
