import random
from pprint import pprint
import emoji
# print(emoji.emojize(':negative_squared_cross_mark:', use_aliases=True), end=" ")



"""CLASSES"""
class Seat:

    def __init__(self, row, seat, reservation, availability):
        self.row = row
        self.seat = seat
        self.reservation = reservation
        self.availability = availability
        # print('Seat Initialized')
class colors:
    HEADER = '\033[95m'
    BLUE = '\033[94m'
    GREEN = '\033[92m'
    RED = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'

"""METHODS"""
def quickSort(list):
    if not list:
        return list
    pivot = list[0]
    lesser = quickSort([x for x in list[1:] if x[1] < pivot[1]])
    greater = quickSort([x for x in list[1:] if x[1] >= pivot[1]])
    return lesser + [pivot] + greater

def printSeatAssignments(seatAssignments):
    i = 0
    for x in range(10):
        print('\n')
        for y in range(20):
            print(seatAssignments[i].seat, end=" ")
            i += 1

def printTheater(seatAssignments):
    i = 0
    for x in range(10):
        print('\n')
        for y in range(20):
            if seatAssignments[i].availability is False:
                print(colors.RED, '1', colors.ENDC, end="")
            else:
                print(colors.GREEN, '0', colors.ENDC, end="")
                
            i += 1

def main():
    reservations = []
    seats = []

    seatAssignments = []
    ticketsSold = 0
    
    with open('sample-input.txt') as f:

        for line in f:
            # rstrip() removes trailing spaces, split(' ') splits line into list at ' '
            reservations.append([x for x in line.rstrip().split(' ')]) 
    
    reservations = quickSort(reservations)

    # Total number of seats reserved (or tickets sold)
    for x in reservations: 
        ticketsSold += int(x[1])
        # Requests of 5 or more seats
        # if int(x[1]) >= 5:
            # print(x[1])
    # print(ticketsSold)




    for row in ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J']:
        for seat in [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]:
            """ @params  (   Row,    Seat,   Reservation Number,   isTaken    ) """
            seatAssignments.append(Seat(row, seat, '', False))

    seatAssignments[199].availability = True
    seatAssignments[129].availability = True
    seatAssignments[9].availability = True
    seatAssignments[82].availability = True
    printTheater(seatAssignments)
    #   Format: ['J', 15, '', 0]

    # pprint(reservations)



main()