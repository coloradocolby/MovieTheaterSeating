# import time

# def quicksort(listToSort, lowIndex, highIndex):
#     if((highIndex - lowIndex) > 0):
#         p = partition(listToSort, lowIndex, highIndex)
#         quicksort(listToSort, lowIndex, p-1)
#         quicksort(listToSort, p+1, highIndex)

# def partition(listToSort, lowIndex, highIndex):
#     divider = lowIndex
#     pivot = highIndex  # This could be anything
#     #   For every element in sublist denoted by lowIndex and highIndex
#     for i in range(lowIndex, highIndex):
#         if(listToSort[i] < listToSort[pivot]):
#             #   Swap these elements of the list
#             listToSort[i], listToSort[divider] = listToSort[divider], listToSort[i]
#             #   Now increment the divider
#             divider += 1
#     listToSort[pivot], listToSort[divider] = listToSort[divider], listToSort[pivot]
#     return divider



# listToSort = random.sample(range(0, 10), 10)
# start_time = time.time()
# quicksort(listToSort, 0, len(listToSort)-1)
# sortingTook = (time.time() - start_time)
# print(listToSort)
# print("--- Sorted in: %s seconds ---" % sortingTook)