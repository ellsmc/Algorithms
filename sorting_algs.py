#______________________________________________________________________________________________________________________________________________________
# BUBBLE SORT
#------------------
# Define function which accepts an array
def bubbleSort(array):
    # Track sorted values.  Last array item will be sorted at start so -1  from array length to get index of last value
    unsortedTilIndex = len(array)-1
    # Iterate through method steps until all items are sorted so use a boolean to montior states
    isSorted = False
    # Until array is not sorted
    while not isSorted:
        # if array is already sorted, no swaps needed
        isSorted = True
        # Here checks if each item in array is sorted
        for i in range(unsortedTilIndex):
            # Comparrison
            if array[i] > array[i+1]:
                # Swap
                array[i], array[i+1] = array[i+1], array[i]
                # if swap was required then array is still unsorted, change boolean 
                isSorted = False
        # Decrememnt as one more item has been sorted
        unsortedTilIndex -= 1
    # When a comparrison runs through without a swap (passthrough) then return sorted array
    return array
