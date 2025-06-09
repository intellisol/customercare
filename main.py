from customer_care.email_receiver import EmailReceiver
from customer_care.data_extractor import DataExtractor
from customer_care.response_agent import ResponseAgent
from customer_care.ticket_creator import TicketCreator
from customer_care.forwarding_agent import ForwardingAgent


def run_workflow() -> None:
    receiver = EmailReceiver()
    extractor = DataExtractor()
    responder = ResponseAgent()
    creator = TicketCreator()
    forwarder = ForwardingAgent(recipients=["support-team@example.com"]) 

    for raw_email in receiver.fetch_emails():
        data = extractor.extract(raw_email)
        if data is None:
            responder.request_more_info(raw_email.get("from", "unknown"))
            continue
        ticket = creator.create_ticket(
            data["customer_email"],
            data["order_reference"],
            data["complaint_description"],
        )
        responder.send_acknowledgement(data["customer_email"], ticket.case_number)
        forwarder.forward(ticket)


if __name__ == "__main__":
    run_workflow()
