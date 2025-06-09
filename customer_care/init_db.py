"""Script to initialize the PostgreSQL database."""

from .config import Config
from .db import get_connection, create_ticket_table


def main():
    config = Config()
    with get_connection(config) as conn:
        create_ticket_table(conn)
        print("Database initialized.")


if __name__ == "__main__":  # pragma: no cover
    main()
