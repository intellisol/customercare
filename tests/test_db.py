from unittest import mock

import psycopg2

from customer_care import db
from customer_care.config import Config


def test_create_ticket_table():
    conn = mock.MagicMock()
    db.create_ticket_table(conn)
    conn.cursor().__enter__().execute.assert_called_with(db.CREATE_TABLE_QUERY)
    conn.commit.assert_called_once()


def test_insert_ticket():
    conn = mock.MagicMock()
    cur = conn.cursor().__enter__()
    cur.fetchone.return_value = [5]
    case = db.insert_ticket(conn, "a@b.c", "123", "desc")
    cur.execute.assert_called()
    conn.commit.assert_called_once()
    assert case == 5


def test_get_connection_calls_psycopg2_connect():
    with mock.patch.object(psycopg2, "connect", return_value="conn") as p:
        cfg = Config()
        result = db.get_connection(cfg)
        assert result == "conn"
        p.assert_called_once()
