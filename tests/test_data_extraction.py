from customer_care import data_extraction as de


def test_extract_success():
    text = """Email: alice@example.com\nOrder: 42\nComplaint: Broken item"""
    ticket = de.extract(text)
    assert ticket
    assert ticket.customer_email == "alice@example.com"
    assert ticket.order_reference == "42"
    assert ticket.complaint_description == "Broken item"


def test_extract_failure():
    text = "No useful data"
    assert de.extract(text) is None
