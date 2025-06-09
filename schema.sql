CREATE TABLE IF NOT EXISTS tickets (
    case_number SERIAL PRIMARY KEY,
    customer_email TEXT NOT NULL,
    order_reference TEXT NOT NULL,
    complaint_description TEXT NOT NULL,
    customer_name TEXT,
    sap_customer TEXT,
    complaint_datetime TIMESTAMP NOT NULL DEFAULT NOW(),
    status TEXT NOT NULL,
    assigned_team TEXT,
    created_timestamp TIMESTAMP NOT NULL DEFAULT NOW(),
    last_updated_timestamp TIMESTAMP NOT NULL DEFAULT NOW()
);
