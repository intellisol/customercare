# Customer Service Agent — Agents Overview

This document outlines the agents and their responsibilities for the in-house Customer Service Agent system that handles customer complaints via Office 365 email.

---

## Agents

### 1. Email Receiver Agent

**Purpose:**  
- Connects to the Office 365 inbox.  
- Receives incoming customer complaint emails in real-time or via polling.

**Responsibilities:**  
- Authenticate and connect to Office 365 email using Microsoft Graph API or suitable protocols.  
- Detect new emails flagged as complaints.  
- Pass raw email content to the Data Extraction Agent.

---

### 2. Data Extraction Agent

**Purpose:**  
- Parse incoming emails to extract essential ticket data fields.

**Responsibilities:**  
- Extract customer email address, order or delivery reference, complaint description, and other relevant info.  
- Validate presence of required fields (e.g., customer email, order/delivery reference).  
- If data is missing, trigger the Response Agent to request more information.  
- Otherwise, forward complete data to the Ticket Creation Agent.

---

### 3. Response Agent

**Purpose:**  
- Generate and send personalized email replies to customers.

**Responsibilities:**  
- If data is incomplete, send a polite, personalized email requesting missing information.  
- When data is complete, send an acknowledgement email with a unique case number and confirmation message.  
- Use customer details to personalize the response.

---

### 4. Ticket Creation Agent

**Purpose:**  
- Create and maintain complaint tickets in the system.

**Responsibilities:**  
- Generate a unique case number for each ticket.  
- Insert ticket details into the complaint management database/table.  
- Update ticket status and timestamps.  
- Notify the Forwarding Agent upon successful ticket creation.

---

### 5. Forwarding Agent

**Purpose:**  
- Forward complaint tickets to internal teams for resolution.

**Responsibilities:**  
- Maintain configurable list of internal recipients (email addresses or groups).  
- Format and forward the ticket details and customer complaint to configured recipients.  
- Log forwarding status and errors if any.

---

## Data Model: Complaint Ticket Table

| Field Name           | Type          | Description                                  |
|----------------------|---------------|----------------------------------------------|
| CaseNumber           | String (Unique) | Unique identifier for the complaint ticket. |
| CustomerEmail        | String        | Email address of the customer.                |
| OrderReference       | String        | Order or delivery reference number.           |
| ComplaintDescription | Text          | Detailed description of the complaint.        |
| CustomerName         | String        | Name of the customer company or contact.      |
| SAPCustomer          | String        | SAP customer identifier (optional).           |
| ComplaintDateTime    | DateTime      | Timestamp of complaint reception.              |
| Status               | String        | Ticket status: New, Pending, Closed, etc.     |
| AssignedTeam         | String        | Internal team or recipient assigned.           |
| CreatedTimestamp     | DateTime      | Timestamp when ticket was created.              |
| LastUpdatedTimestamp | DateTime      | Timestamp of last ticket update.                 |

---

## Workflow Summary

1. **Email Receiver Agent** collects new complaint emails.  
2. **Data Extraction Agent** extracts and validates required information.  
3. **Response Agent** contacts customer to request missing info or acknowledge receipt with case number.  
4. **Ticket Creation Agent** creates a ticket once all required data is available.  
5. **Forwarding Agent** sends the ticket details to internal teams configured in the system.

---

This modular agent design enables an efficient, automated complaint management system with human-like customer communication and internal routing flexibility.

