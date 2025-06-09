from customer_care import data_extraction as de


def test_extract_success():
    text = (
        "Email: alice@example.com\n"
        "Order: 42\n"
        "Complaint: Broken item\n"
        "Name: Nestle\n"
        "SAP Customer: C123\n"
    )
    ticket = de.extract(text)
    assert ticket
    assert ticket.customer_email == "alice@example.com"
    assert ticket.order_reference == "42"
    assert ticket.complaint_description == "Broken item"
    assert ticket.customer_name == "Nestle"
    assert ticket.sap_customer == "C123"


def test_extract_failure():
    text = "No useful data"
    assert de.extract(text) is None
