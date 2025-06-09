"""Data Extraction Agent."""
from __future__ import annotations

from typing import Optional, TypedDict


class ExtractedData(TypedDict, total=False):
    customer_email: str
    order_reference: str
    complaint_description: str


class DataExtractor:
    def extract(self, raw_email: dict) -> Optional[ExtractedData]:
        """Extract required fields from a raw email dictionary."""
        body = raw_email.get("body", "")
        lines = body.splitlines()
        order_ref = None
        description_lines = []
        for line in lines:
            if line.lower().startswith("orderreference:"):
                order_ref = line.split(":", 1)[1].strip()
            else:
                description_lines.append(line)
        complaint_desc = "\n".join(description_lines).strip()

        if raw_email.get("from") and order_ref:
            return ExtractedData(
                customer_email=raw_email["from"],
                order_reference=order_ref,
                complaint_description=complaint_desc,
            )
        return None
