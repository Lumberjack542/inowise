import unittest
from ticket.models import Ticket


class TicketTestCase(unittest.TestCase):
    def set_uo(self):
        self.title = Ticket.objects.create(name='tets1')