from abc import ABC, abstractmethod
from datetime import datetime


class Ticket:
    def __init__(self, id: int, price: float, place: int, date_time: datetime, is_valid: bool):
        self.id = id
        self.price = price
        self.place = place
        self.date_time = date_time
        self.is_valid = is_valid


class ITicketRepo(ABC):
    @abstractmethod
    def create(self, ticket: Ticket) -> bool:
        pass

    @abstractmethod
    def search(self, date_time: datetime, city: str) -> [Ticket]:
        pass

    @abstractmethod
    def update(self, ticket: Ticket, new_status: bool) -> bool:
        pass

    @abstractmethod
    def delete(self, ticket: Ticket) -> bool:
        pass


class TicketRepository(ITicketRepo):
    def __init__(self):
        self.repo = [Ticket]

    def create(self, ticket: Ticket) -> bool:
        pass

    def search(self, date_time: datetime, city: str) -> [Ticket]:
        pass

    def update(self, ticket: Ticket, new_status: bool) -> bool:
        pass

    def delete(self, ticket: Ticket) -> bool:
        pass


class TicketProvider:
    def __init__(self):
        self.ticket_repo = TicketRepository()

    def find_tickets(self, date_time: datetime, city: str) -> [Ticket]:
        return self.ticket_repo.search(date_time, city)

    def get_tickets(self, ticket: Ticket, count: int) -> [Ticket]:
        self.ticket_repo.update(ticket, False)
        return [Ticket]

