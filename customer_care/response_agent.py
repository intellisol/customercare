"""Generate customer responses."""

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
    return ACK_TEMPLATE.format(email=ticket.customer_email, case=case_number)


def request_more_info(email: str) -> str:
    return REQ_TEMPLATE.format(email=email)
