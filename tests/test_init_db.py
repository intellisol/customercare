from unittest import mock

from customer_care import init_db


def test_main_calls_create_table():
    with mock.patch("customer_care.init_db.get_connection") as gc, \
         mock.patch("customer_care.init_db.create_ticket_table") as ctt:
        gc.return_value.__enter__.return_value = "conn"
        init_db.main()
        gc.assert_called_once()
        ctt.assert_called_once_with("conn")
