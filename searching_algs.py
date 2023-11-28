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
