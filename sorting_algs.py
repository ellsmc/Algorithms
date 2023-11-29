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
#_____________________________________________________________________________________________________________________________________________________
# MERGE SORT
#------------------
def merge_sort(list):
    """
    Sort into ascending order
    Out: new sorted list
    Divide to find midpt and sublists
    Recursively sort sublists
    Merge sorted sublists
    O(kn log n)
    """
    # Naively sorted conditions
    if len(list) <= 1:
        return list
    
    left_half, right_half = split(list)
    left = merge_sort(left_half)
    right = merge_sort(right_half)

    return merge(left, right)

def split(list):
    """
    Divide unsorted list at midpt into sublists
    Return sublists (left, right)
    splitting is constant time k
    O(k log n) time
    """
    mid = len(list)//2
    left = list[:mid]
    right = list[mid:]

    return left, right

def merge(left, right):
    """
    Merges two lists(arrays), sorts them
    Returns new merged list
    O(n)
    """
    l = []
    i = 0
    j = 0

    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            l.append(left[i])
            i += 1
        else:
            l.append(right[j])
            j += 1
    while i < len(left):
        l.append(left[i])
        i+=1
    while j < len(right):
        l.append(right[j])
        j+=1
    return l

def verify(list):
    n = len(list)
    if n == 0 or n == 1:
        return True
    return list[0] < list[1] and verify(list[1:])

sortme = [ 43, 7, 3, 222, 9, 14, 12, 6]
l = merge_sort(sortme)
# print(l)
print(verify(sortme))
print(verify(l))
