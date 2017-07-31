"""CLASSES"""

class Reservation:

    def __init__(self, name, quantity):
        self.name = name
        self.quantity = quantity
        self.seats = []
        self.fulfilled = False

class Seat:
    def __init__(self, row, chair, availability):
        self.row = row
        self.chair = chair
        self.reservation = None
        self.availability = availability

class Row:

    def __init__(self, seats):
        self.seats = seats

class Colors:

    HEADER = '\033[95m'
    BLUE = '\033[94m'
    GREEN = '\033[92m'
    RED = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'

    def __init__(self):
        pass

