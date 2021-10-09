class Passenger:
    ticket: bool

    def __init__(self, ticket: bool = True):
        self.ticket = ticket

    def __repr__(self):
        return f'| Ticket: {self.ticket} |'
