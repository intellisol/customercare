"""Response Agent."""
from __future__ import annotations

from typing import Any


class ResponseAgent:
    def request_more_info(self, customer_email: str) -> Any:
        """Send an email requesting missing information."""
        # Placeholder for sending email
        print(f"Requesting more info from {customer_email}")

    def send_acknowledgement(self, customer_email: str, case_number: str) -> Any:
        """Send acknowledgement email with case number."""
        # Placeholder for sending email
        print(
            f"Acknowledgement sent to {customer_email} for case {case_number}"
        )
