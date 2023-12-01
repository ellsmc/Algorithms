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
# print(verify(sortme))
# print(verify(l))

###############################
# MERGE SORT - LINKED LIST
# O(n log n)
#------------------
from lists import LinkedList

def merge_sort_LL(linked_list):
    """
    Returns sorted linked list
    """
    if linked_list.size() == 1:
        return linked_list
    elif linked_list.head is None:
        return linked_list
    
    left_half, right_half = split_LL(linked_list)
    left = merge_sort_LL(left_half)
    right = merge_sort_LL(right_half)

    return merge_LL(left, right)

def split_LL(linked_list):

    if linked_list == None or linked_list.head == None:
        left_half = linked_list
        right_half = None

        return left_half, right_half
    else:
        size = linked_list.size()
        mid = size//2
        mid_node = linked_list.value_at_index(mid-1)

        left_half = linked_list
        right_half = LinkedList()
        right_half.head = mid_node.next_node
        mid_node.next_node = None

        return left_half, right_half
    
def merge_LL(left, right):
    """
    Merges two LL sorting by data in nodes
    Returns new merged list
    """
    # New LL to take L,R nodes
    merged = LinkedList()
    # Add fake head to be discarded later
    merged.add(0)
    current = merged.head
    left_head = left.head
    right_head = right.head
    # Iterate over L, R until tail nodes
    while left_head or right_head:
        # If heads are None then past tail of each list, add remaining nodes to list
        if left_head is None:
            current.next_node = right_head
            right_head = right_head.next_node
        elif right_head is None:
            current.next_node = left_head
            left_head = left_head.next_node
        else:
            # Not at either tail node
            left_data = left_head.data
            right_data = right_head.data
            # Comparison operations
            if left_data < right_data:
                current.next_node = left_head
                left_head = left_head.next_node
            else:
                current.next_node = right_head
                right_head = right_head.next_node
        current = current.next_node
    # Discard fake head
    head = merged.head.next_node
    merged.head = head
    return merged
        
def verify_LL():
    pass

LL = LinkedList()
LL.add(1)
LL.add(15)
LL.add(24)
LL.add(10)
LL.add(67)
LL.add(8)
LL.add(123)
print(LL)
sorted_LL = merge_sort_LL(LL)
print(sorted_LL)


###############################
# MERGE SORT - RECURSIVE
#------------------

def merge_recursive(values):
    # Base case
    if len(values) <=1:
        return values
    mid_index = len(values)//2 # Floor // divides and rounds down
    left_values = merge_recursive(values[:mid_index])
    right_values = merge_recursive(values[mid_index:])
    # print("%15s %-15s" % (left_values, right_values))
    sorted = []
    left_ind = 0
    right_ind = 0
    while left_ind < len(left_values) and right_ind < len(right_values):
        if left_values[left_ind] < right_values[right_ind]:
            sorted.append(left_values[left_ind])
            left_ind += 1
        else:
            sorted.append(right_values[right_ind])
            right_ind += 1
    sorted += left_values[left_ind:]
    sorted += right_values[right_ind:]
    return sorted

sorted_nums = merge_recursive(sortme)
print("Recursive merge: ", sorted_nums)


#______________________________________________________________________________________________________________________________________________________
# SELECTION SORT
# O(n2)
#------------------
import sys
from load import load_numbers

# numbers = load_numbers(sys.argv[1])
# numbers = [4, 68, 90, 43, 3 ,7, 8, 9]

def index_of_min(values):
    min_index = 0
    for i in range(1, len(values)):
        if values[i] < values[min_index]:
            min_index = i
    return min_index

def selection_sort(values):
    sorted_list = []
    # print("%-25s %-25s" % (values, sorted_list))
    for i in range(0, len(values)):
        index_to_move = index_of_min(values)
        sorted_list.append(values.pop(index_to_move))
        # print("%-25s %-25s" % (values, sorted_list))
    return sorted_list

#print(selection_sort(numbers))

"""
terminal> time python sorting_algs.py unsorted_nums.txt
0.00user 0.01system 0:00.09elapsed 15%CPU (0avgtext+0avgdata 5352maxresident)k
0inputs+0outputs (1389major+0minor)pagefaults 0swaps

user+sys to evaluate runtime
"""

#______________________________________________________________________________________________________________________________________________________
# QUICK SORT
# BC O(n logn)
# WC O(n2)
# Need to use a random pivot
#------------------

numbers_small = [1, 5, 7, 24, 46, 96, 45, 8, 5, 432, 654, 76, 32, 65, 13, 75]

def quick_sort(values):
    if len(values) <= 1:
        return values
    less_than_pivot = []
    greater_than_pivot = []
    pivot = values[0]
    for value in values[1:]:
        if value <= pivot:
            less_than_pivot.append(value)
        else:
            greater_than_pivot.append(value)
            # print("%15s %1s %-15s" % (less_than_pivot, pivot, greater_than_pivot))
    return quick_sort(less_than_pivot) + [pivot] + quick_sort(greater_than_pivot)

print(quick_sort(numbers_small))

#______________________________________________________________________________________________________________________________________________________
#  SORT
#------------------


#______________________________________________________________________________________________________________________________________________________
#  SORT
#------------------