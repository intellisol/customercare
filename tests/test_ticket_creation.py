from unittest import mock

from customer_care.ticket_creation import create_ticket
from customer_care.data_extraction import TicketData
from customer_care.config import Config


def test_create_ticket_calls_db():
    ticket = TicketData("a@b.c", "1", "desc")
    config = Config()
    with mock.patch("customer_care.ticket_creation.db") as db_mock:
        db_mock.get_connection.return_value.__enter__.return_value = "conn"
        db_mock.insert_ticket.return_value = 7
        case = create_ticket(ticket, config)
        db_mock.get_connection.assert_called_once_with(config)
        db_mock.insert_ticket.assert_called_once()
        assert case == 7
