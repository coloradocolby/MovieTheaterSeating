"""
QUICKSORT

O(n log n)

[1, 4, 5, 7, 0, 6, 2, 8, 9, 3]

Take random number out of the list you are trying to sort.

This is the PIVOT.

Once we choose the pivot we compare it to each element in the list.

Once the comparison is finished, the pivot will end up in the position
that it would be in if the list was sorted

In addition, all the numbers to the left of the pivot will be less than the pivot
and all the numbers to the right will be greater.

This is called PARTITIONING

Once the partitioning is complete, we will have two lists aboe and below the pivot,
that themselves need to be partitioned

Because we are partitioning over and over, we should use RECURSION

We will create a function that calls itself multiple times and goes through and sorts this list


PARTITIONING

So 3 is the pivot (random choice). Is it greater than or less than the first element
(1).

[1, 4, 5, 7, 0, 6, 2, 8, 9, 3]

When we start this comparison we have one more value we need to keep track of

We will call this the DIVIDER POSITION for the PIVOT element. The DIVIDER for short.

The divider will be the first element int he list to begin with, when we find an element in the
list that is less than the pivot, we will then swap that element with the divider and
make the next element in the list the new divider. 1 is less than 3

but the DIVIDER is 1 so we swap 1 with itself, and the DIVIDER will now be at 4.

4 is greater than 3 so we keep going. 5 and 7 are greater than 3. 0 is less than 3 so take
0 and swap it with 4.

which is our current DIVIDER.

Increment the DIVIDER.

The DIVIDER is now 5

6 is not less than 3, 2 is less than 3, so swap 2 with 5

The next two elements in the list, 8 and 9 are less than three

[1, 0, 2, 7, 4, 6, 5, 7, 9, 3]

Now swap 3 with 7

Everything to the left of 3 is less than and everything to the right is greater than
"""

import random
import time

def quicksort(listToSort, lowIndex, highIndex):
    """
    Stopping condition: when low and high index are the same
    """
    if((highIndex - lowIndex) > 0):
        p = partition(listToSort, lowIndex, highIndex)
        print(listToSort)
        """
        This gives us two lists to sort so we now need to  call quicksort twice

        we know p is in the right position so sort everything under it
        """
        quicksort(listToSort, lowIndex, p-1)

        """
        NOTE this second function call to quicksort does not occur
        until the entire recursion tree for the first call is finished

        Sort list starting at what is above p as well
        """
        quicksort(listToSort, p+1, highIndex)

def partition(listToSort, lowIndex, highIndex):
    """
    Bulk of the work happens here.

    Things we need to keep track of here
        PIVOT
        DIVIDER
    """

    divider = lowIndex
    print('Divider is ', listToSort[divider])
    pivot = highIndex  # This could be anything
    print('Pivot is ', listToSort[pivot])

    #   For every element in sublist denoted by lowIndex and highIndex
    for i in range(lowIndex, highIndex):
        if(listToSort[i] < listToSort[pivot]):
            print(listToSort[i], '<', listToSort[pivot])
            #   Swap these elements of the list
            listToSort[i], listToSort[divider] = listToSort[divider], listToSort[i]
            #   Now increment the divider
            divider += 1
        else:
            print('pass')

    """
    Once we've gone through this ^ and swapped as appropriate, we need to
    swap the pivot with the divider
    """
    print('Swapping', listToSort[pivot], 'with', listToSort[divider])
    listToSort[pivot], listToSort[divider] = listToSort[divider], listToSort[pivot]
    return divider


# testlist = random.sample(range(0, 100), 100)
testlist = [1, 4, 5, 7, 0, 6, 2, 8, 9, 3] 
print('UNSORTED')
print(testlist)

# start_time = time.time()

quicksort(testlist, 0, len(testlist)-1)
# sortingTook = (time.time() - start_time)

# print('\n\nSORTED\n\n', testlist)
# print("--- Sorted in: %s seconds ---" % sortingTook)

# # REVERSE TEST
# reverse =  [99, 98, 97, 96, 95, 94, 93, 92, 91, 90, 89, 88, 87, 86, 85, 84, 83, 82, 81, 80, 79, 78, 77, 76, 75, 74, 73, 72, 71, 70, 69, 68, 67, 66, 65, 64, 63, 62, 61, 60, 59, 58, 57, 56, 55, 54, 53, 52, 51, 50, 49, 48, 47, 46, 45, 44, 43, 42, 41, 40, 39, 38, 37, 36, 35, 34, 33, 32, 31, 30, 29, 28, 27, 26, 25, 24, 23, 22, 21, 20, 19, 18, 17, 16, 15, 14, 13, 12, 11, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1, 0]

# start_time = time.time()

# quicksort(reverse, 0, len(reverse)-1)
# sortingTook = (time.time() - start_time)

# print('\n\nREVERSE SORTED\n\n', reverse)
# print("--- Sorted in: %s seconds ---" % sortingTook)
