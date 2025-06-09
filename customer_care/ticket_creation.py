"""Create tickets in the database."""

from . import db
from .config import Config
from .data_extraction import TicketData


def create_ticket(ticket: TicketData, config: Config) -> int:
    with db.get_connection(config) as conn:
        case_number = db.insert_ticket(
            conn,
            ticket.customer_email,
            ticket.order_reference,
            ticket.complaint_description,
            status="New",
            assigned_team=None,
        )
        return case_number
