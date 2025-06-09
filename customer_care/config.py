from dataclasses import dataclass, field
import os
import json

@dataclass
class Config:
    """Configuration for the customer care system."""
    email_user: str = os.getenv("CC_EMAIL_USER", "user@example.com")
    email_password: str = os.getenv("CC_EMAIL_PASSWORD", "changeme")
    inbox_id: str = os.getenv("CC_EMAIL_INBOX_ID", "inbox@example.com")
    recipients: list = field(default_factory=lambda: json.loads(os.getenv("CC_RECIPIENTS", '["support@example.com"]')))
    db_host: str = os.getenv("CC_DB_HOST", "localhost")
    db_port: int = int(os.getenv("CC_DB_PORT", "5432"))
    db_name: str = os.getenv("CC_DB_NAME", "customercare")
    db_user: str = os.getenv("CC_DB_USER", "ccuser")
    db_password: str = os.getenv("CC_DB_PASSWORD", "changeme")
