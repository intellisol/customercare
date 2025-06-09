"""Database utilities for PostgreSQL."""

import psycopg2
from psycopg2 import sql
from .config import Config

CREATE_TABLE_QUERY = sql.SQL(
    """CREATE TABLE IF NOT EXISTS tickets (
        case_number SERIAL PRIMARY KEY,
        customer_email TEXT NOT NULL,
        order_reference TEXT NOT NULL,
        complaint_description TEXT NOT NULL,
        complaint_datetime TIMESTAMP NOT NULL DEFAULT NOW(),
        status TEXT NOT NULL,
        assigned_team TEXT,
        created_timestamp TIMESTAMP NOT NULL DEFAULT NOW(),
        last_updated_timestamp TIMESTAMP NOT NULL DEFAULT NOW()
    );"""
)

INSERT_TICKET_QUERY = sql.SQL(
    """INSERT INTO tickets (
        customer_email,
        order_reference,
        complaint_description,
        status,
        assigned_team
    ) VALUES (%s, %s, %s, %s, %s) RETURNING case_number;"""
)


def get_connection(config: Config):
    """Create a database connection based on the provided config."""
    return psycopg2.connect(
        host=config.db_host,
        port=config.db_port,
        dbname=config.db_name,
        user=config.db_user,
        password=config.db_password,
    )


def create_ticket_table(conn):
    """Create the tickets table if it doesn't exist."""
    with conn.cursor() as cur:
        cur.execute(CREATE_TABLE_QUERY)
    conn.commit()


def insert_ticket(conn, customer_email, order_reference, complaint_description, status="New", assigned_team=None):
    """Insert a ticket into the database and return the generated case number."""
    with conn.cursor() as cur:
        cur.execute(
            INSERT_TICKET_QUERY,
            (customer_email, order_reference, complaint_description, status, assigned_team),
        )
        case_number = cur.fetchone()[0]
    conn.commit()
    return case_number
