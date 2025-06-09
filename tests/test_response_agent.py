from customer_care.response_agent import acknowledgement, request_more_info
from customer_care.data_extraction import TicketData


def test_acknowledgement():
    ticket = TicketData("a@b.c", "123", "Broken")
    msg = acknowledgement(ticket, 1)
    assert "case number is 1" in msg
    assert "a@b.c" in msg


def test_request_more_info():
    msg = request_more_info("a@b.c")
    assert "more information" in msg
