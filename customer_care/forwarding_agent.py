"""Forward tickets to internal recipients."""

from .config import Config
from .data_extraction import TicketData


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
