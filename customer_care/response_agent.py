
"""Generate and send customer responses."""

from __future__ import annotations

import smtplib
from typing import Any

from .config import Config
from .data_extraction import TicketData


ACK_TEMPLATE = (
    "Dear {email},\n\n"
    "Thank you for contacting us. Your case number is {case}. We will respond soon."
)

REQ_TEMPLATE = (
    "Dear {email},\n\n"
    "We need more information to process your complaint. Please provide order reference and description."
)


def acknowledgement(ticket: TicketData, case_number: int) -> str:
    """Return acknowledgement email body for a ticket."""
    return ACK_TEMPLATE.format(email=ticket.customer_email, case=case_number)


def request_more_info(email: str) -> str:
    """Return body requesting more information from the customer."""
    return REQ_TEMPLATE.format(email=email)


def send_email(recipient: str, body: str, config: Config) -> None:
    """Send an email using ``smtplib`` based on the provided configuration."""
    message = f"From: {config.email_user}\nTo: {recipient}\n\n{body}"
    with smtplib.SMTP("localhost") as smtp:
        smtp.login(config.email_user, config.email_password)
        smtp.sendmail(config.email_user, [recipient], message)


class ResponseAgent:
    def __init__(self, config: Config | None = None) -> None:
        self.config = config or Config()

    def request_more_info(self, customer_email: str) -> Any:
        """Send an email requesting missing information."""
        body = REQ_TEMPLATE.format(email=customer_email)
        send_email(customer_email, body, self.config)

    def send_acknowledgement(self, customer_email: str, case_number: str) -> Any:
        """Send acknowledgement email with case number."""
        body = ACK_TEMPLATE.format(email=customer_email, case=case_number)
        send_email(customer_email, body, self.config)
