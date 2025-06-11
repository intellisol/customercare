from unittest import mock

from customer_care.response_agent import (
    acknowledgement,
    request_more_info,
    ResponseAgent,
)
from customer_care.data_extraction import TicketData
from customer_care.config import Config


def test_acknowledgement():
    ticket = TicketData("a@b.c", "123", "Broken")
    msg = acknowledgement(ticket, 1)
    assert "case number is 1" in msg
    assert "a@b.c" in msg


def test_request_more_info():
    msg = request_more_info("a@b.c")
    assert "more information" in msg


def test_response_agent_emails():
    agent = ResponseAgent(Config())
    with mock.patch("customer_care.response_agent.send_email") as send_mock:
        agent.send_acknowledgement("c@example.com", "5")
        send_mock.assert_called_once()
        args = send_mock.call_args[0]
        assert args[0] == "c@example.com"
        assert "case number is 5" in args[1]


def test_request_email_via_agent():
    agent = ResponseAgent(Config())
    with mock.patch("customer_care.response_agent.send_email") as send_mock:
        agent.request_more_info("d@example.com")
        send_mock.assert_called_once()
        args = send_mock.call_args[0]
        assert args[0] == "d@example.com"
        assert "more information" in args[1]
