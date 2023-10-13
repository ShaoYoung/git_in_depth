from user import User, UserProvider
from ticket import Ticket, TicketProvider
from cash import CashProvider
from datetime import datetime


class Customer:
    def __init__(self, user: User):
        self.user_provider = UserProvider()
        self.user = user
        self.cash_provider = CashProvider()
        self.ticket_provider = TicketProvider()
        self.tickets = []

    def search_tickets(self, date_time: datetime, count: int) -> [Ticket]:
        pass

    def buy_ticket(self, ticket: Ticket, count: int) -> bool:
        self.tickets.extend(self.ticket_provider.get_tickets(ticket, count))
        return True
