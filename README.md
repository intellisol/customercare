# Customer Care

This project demonstrates a very small customer care system based on the agent workflow described in `AGENTS.md`.  It uses a PostgreSQL database for storing complaint tickets.

## Configuration

Configuration is handled by `customer_care.config.Config`.  Values can be customised via environment variables or by editing the file directly.

| Environment Variable | Purpose |
|---------------------|---------|
| `CC_EMAIL_USER` | Email account used for sending messages |
| `CC_EMAIL_PASSWORD` | Password for the above account |
| `CC_EMAIL_INBOX_ID` | Inbox identifier to monitor |
| `CC_RECIPIENTS` | JSON list of internal recipient emails |
| `CC_DB_HOST` | PostgreSQL host |
| `CC_DB_PORT` | PostgreSQL port |
| `CC_DB_NAME` | Database name |
| `CC_DB_USER` | Database user |
| `CC_DB_PASSWORD` | Password for the database user |

## Database

Run the `customer_care/init_db.py` script to create the `tickets` table in your PostgreSQL instance. The table includes optional `customer_name` and `sap_customer` columns for storing customer details when available:

```bash
python -m customer_care.init_db
```

The SQL used by the script is also provided in `schema.sql` if you prefer running it manually.

## Development

Install dependencies and run the tests with coverage:

```bash
pip install -r requirements.txt
PYTHONPATH=. pytest --cov=customer_care
```

The tests cover every module to ensure 100% coverage.
