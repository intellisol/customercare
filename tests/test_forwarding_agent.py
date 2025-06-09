from customer_care.forwarding_agent import format_forward, recipients
from customer_care.data_extraction import TicketData
from customer_care.config import Config


def test_format_forward():
    ticket = TicketData("a@b.c", "123", "issue")
    msg = format_forward(ticket, 2)
    assert "ticket 2" in msg
    assert "issue" in msg


def test_recipients_default():
    config = Config()
    rcpts = recipients(config)
    assert isinstance(rcpts, list)
    assert rcpts
