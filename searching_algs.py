# Linear search
# O(n) complexity (Linear)
def linear_search(list, target):
	"""
	Returns index of target. Else returns none - could also raise exception?
	"""
	for index in range(0, len(list)): # could it be 'for value in len(list)?
		if list[index] == target:
			return index
	return None
def verify(index):
	if index is not None:
		print("Tagret found at index: ", index)
	else:
		print("Target is not in list")
		
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
result = linear_search(numbers, 12)
verify(result)
result = linear_search(numbers, 8)
verify(result)

# Binary search
# O(log n) complexity (Logarithmic)
def binary_search(list, target):
	first = 0
	last = len(list) - 1

	while first <= last:
		midpoint = (first + last) //2   #floor division to round to number
		if list[midpoint] == target:
			return midpoint
		elif list[midpoint] < target:
			first = midpoint + 1
		else:
			last = midpoint - 1
	return None
result = binary_search(numbers, 15)
verify(result)
result = binary_search(numbers, 5)
verify(result)
