from dataclasses import dataclass, field
from datetime import datetime
import uuid

@dataclass
class ComplaintTicket:
    customer_email: str
    order_reference: str
    complaint_description: str
    complaint_datetime: datetime
    status: str = "New"
    assigned_team: str = "Unassigned"
    case_number: str = field(default_factory=lambda: uuid.uuid4().hex)
    created_timestamp: datetime = field(default_factory=datetime.utcnow)
    last_updated_timestamp: datetime = field(default_factory=datetime.utcnow)

    def update_status(self, new_status: str, team: str | None = None) -> None:
        self.status = new_status
        if team:
            self.assigned_team = team
        self.last_updated_timestamp = datetime.utcnow()
