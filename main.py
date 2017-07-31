import sys, os, time
from models import Reservation, Seat, Row, Colors

"""METHODS"""

def assign_seats(reservations, rows):

    for row in reversed(rows):

        seat_counter = 0
        row_capacity = len(row.seats)

        for res in reservations:

            if res.quantity <= row_capacity and not res.fulfilled:

                for x in range(res.quantity):
                    # if row.seats[seat_counter].availability:
                        current_seat = row.seats[seat_counter]

                        current_seat.reservation = res
                        current_seat.availability = False

                        res.seats.append(current_seat)
                        res.fulfilled = True
                        seat_counter += 1
                        row_capacity -= 1

# Disable Printing
def block_print():
    sys.stdout = open(os.devnull, 'w')

# Restore Printing
def enable_print():
    sys.stdout = sys.__stdout__

def get_reservations(reservations):
    output = ''
    for reservation in reservations:
        output += reservation.name + ' '
        for seat in reservation.seats:
            output += seat.row + str(seat.chair) + "," # comma delimted

        output = output[:-1] # [:-1] removes final ','
        output += '\n'

    return output[:-1] # [:-1] removes final '\n'

def get_total_reservations(reservations):
    total = 0
    for x in reservations:
        total += x.quantity
    return total

def print_success(message):
    print(Colors.BOLD + Colors.GREEN + message + Colors.ENDC, end="\n\n")

def print_theater(rows):

    for row in rows:
        for seat in row.seats:
            if seat.availability is False:
                print(Colors.GREEN + seat.row + str(seat.chair) + Colors.RED + seat.reservation.name + Colors.ENDC, end=" ")
            else:
                print(Colors.GREEN + "  " + seat.row + str(seat.chair) + "  " + Colors.ENDC, end=" ")
        print('\n')


def print_warning(message):
    print(Colors.BOLD + Colors.RED + message + Colors.ENDC, end="\n")


def runtests(reservations, rows, disable_printing):

    if disable_printing:
        block_print()

    print_success('Running Tests...')
    all_tests_passed = True

    # Test 1 - Sufficient Number of Seats
    print_success('Test 1 - Sufficient Number of Seats')
    if get_total_reservations(reservations) > 200:
        print_warning('FAILED')
        all_tests_passed = False
    else:
        print_success('PASSED')

    # Test 2 - Valid Reservation Format
    print_success('Test 2 - Valid Reservation Format')

    try:
        inFile = sys.argv[1]
        with open(inFile, 'r') as i:

            for line in i:
                # rstrip() removes trailing spaces, split(' ') splits line into list at ' '
                # reservations.append([x for x in line.rstrip().split(' ')])
                reservation = line.rstrip().split(' ')
                if reservation[0].startswith('R') and int(reservation[1]) < 20:
                    reservations.append(Reservation(reservation[0], int(reservation[1])))
                else:
                    raise ValueError
        print_success('PASSED')

    except OSError:
        print_warning('FAILED \t Unable to find Input File')
        all_tests_passed = False
    except IndexError:
        print_warning('FAILED \t Please supply path to Input File')
        all_tests_passed = False
    except UnicodeDecodeError:
        print_warning('FAILED \t Unrecognized File Type')
        all_tests_passed = False
    except ValueError:
        print_warning('FAILED \t Error in Input File Format')
        all_tests_passed = False
    except:
        print_warning('FAILED \t An unknown error has occured')
        all_tests_passed = False

    # SUCCESSFULLY PASSED ALL TESTS
    if all_tests_passed:
        print_success('ALL TESTS PASSED')
        enable_print()
        return True
    else:
        enable_print()
        return False

def process_reservations(reservations, rows, final_reservations):
    if runtests(reservations, rows, True):
        assign_seats(reservations, rows)
        final_reservations = get_reservations(reservations)

        with open('output.txt', 'w') as o:
            o.write(final_reservations)

        print(Colors.BOLD + Colors.BLUE + 'Output file is availabile at', Colors.GREEN, os.getcwd() + '/output.txt' + Colors.ENDC)

    else:
        print_warning('Tests failed. Unable to process reservations.')

def main():

    reservations = []
    final_reservations = ''
    rows = []
    rows_list = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J']
    chairs_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]

    # propagate rows
    for x in rows_list:
        row = Row([])
        for y in chairs_list:
            row.seats.append(Seat(x, y, True))
        rows.append(row)

    # sort by quantity
    reservations.sort(key=lambda x: x.quantity)
    # reverse so highest quantity is on top
    reservations = list(reversed(reservations))


    if len(sys.argv) > 2:
        if sys.argv[2] == 'showtheater':
            process_reservations(reservations, rows, final_reservations)
            print_theater(rows)
        elif sys.argv[2] == 'runtests':
            runtests(reservations, rows, False)
        else:
            print(Colors.BOLD + Colors.RED + 'Invalid Argument:', sys.argv[2] + Colors.ENDC)
    else:
        process_reservations(reservations, rows, final_reservations)


main()
