from customer_care.email_receiver import EmailReceiver


def test_receive_returns_list():
    r = EmailReceiver("inbox")
    assert list(r.receive()) == []
