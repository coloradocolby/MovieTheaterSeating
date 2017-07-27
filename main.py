import random
from pprint import pprint

def quickSort(list):
    if not list:
        return list
    pivot = list[0]
    lesser = quickSort([x for x in list[1:] if x[1] < pivot[1]])
    greater = quickSort([x for x in list[1:] if x[1] >= pivot[1]])
    return lesser + [pivot] + greater

def main():
    reservations = []
    ticketsSold = 0
    
    with open('sample-input.txt') as f:

        for line in f:
            reservations.append([x for x in line.rstrip().split(' ')]) #    rstrip() removes trailing spaces, split(' ') splits line into list at ' '

        reservations = quickSort(reservations)

        for x in reservations: ticketsSold += int(x[1])
        print(ticketsSold)
main()
