#______________________________________________________________________________________________________________________________________________________
# LINEAR SEARCH
# O(n) complexity (Linear)
#------------------

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
# result = linear_search(numbers, 12)
# verify(result)
# result = linear_search(numbers, 8)
# verify(result)


###############################
# LINEAR SEARCH - STRINGS
#  O(n)
#------------------
import sys
from load import load_strings

# names = load_strings(sys.argv[1])
search_names = ["Lucie Hansman", "Mariann Melena",  "Sibyl Froeschle", "Ray Spratling"]
names = ["Francina Vigneault", "Lucie Hansman", "Nancie Rubalcaba", "Elida Sleight", "Guy Lashbaugh", "Ginger Schlossman", "Suellen Luaces", "Jamey Kirchgesler", "Amiee Elwer", "Lacresha Peet", "Leonia Goretti", "Carina Bunge", "Renee Brendeland", "Andrew Mcgibney", "Gina Degon", "Deandra Pihl", "Desmond Steindorf", "Magda Growney", "Tawana Srivastava", "Tammi Todman", "Harley Mussell", "Iola Bordenet", "Edwardo Khela", "Myles Deanne", "Elden Dohrman", "Ira Hooghkirk", "Eileen Stigers", "Mariann Melena", "Maryrose Badura", "Ardelia Koffler", "Lacresha Kempker", "Charlyn Singley", "Lekisha Tawney", "Christena Botras", "Mike Blanchet", "Cathryn Hinkson", "Errol Shinkle", "Mavis Bhardwaj", "Sung Filipi", "Keiko Dedeke", "Lorelei Morrical", "Jimmie Lessin", "Adrianne Hercules", "Latrisha Haen", "Denny Friedeck", "Emmett Whitesell", "Sina Sauby", "Melony Engwer", "Alina Reichel", "Rosamond Shawe", "Elinore Benyard", "Sang Bouy", "Ed Aparo", "Sheri Wedding", "Sang Snellgrove", "Shaquana Sones", "Elvia Motamed", "Candice Lucey", "Sibyl Froeschle", "Ray Spratling", "Cody Mandeville", "Donita Cheatham", "Darren Later", "Johnnie Stivanson", "Enola Kohli", "Leann Muccia", "Carey Philps", "Suellen Tohonnie", "Evelynn Delucia", "Luz Kliment", "Lettie Jirjis", "Francene Klebe", "Margart Scholz", "Sarah Growden", "Glennis Gines", "Rachael Ojima", "Teofila Stample", "Narcisa Shanley", "Gene Lesnick", "Malena Applebaum", "Norma Tingey", "Marianela Mcmullen", "Rosalva Dosreis", "Dallas Heinzmann", "Sade Streitnatter", "Lea Pelzel", "Judith Zwahlen", "Hope Vacarro", "Annette Ayudan", "Irvin Cyree", "Scottie Levenstein", "Agustina Kobel", "Kira Moala", "Fawn Englar", "Jamal Gillians", "Karen Lauterborn", "Kit Karratti", "Steven Deras", "Mary Rosenberger", "Alonso Viviano"]

def index_of_item(collection, target):
	for i in range(0, len(collection)):
		if target == collection[i]:
			return i
	return None

# for n in search_names:
# 	index = index_of_item(names, n)
# 	print(index)

#______________________________________________________________________________________________________________________________________________________
# BINARY SEARCH
# O(log n) complexity (Logarithmic), constant space
#------------------

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
# result = binary_search(numbers, 15)
# verify(result)
# result = binary_search(numbers, 5)
# verify(result)

###############################
# BINARY SEARCH - RECURSIVE
#  Time O(log n)
#------------------

def recursive_binary_search(list, target):
	if len(list) == 0:
		return False
	else:
		midpoint = (len(list)//2)
		if list[midpoint] == target:
			return True
		else:
			if list[midpoint] < target:
				return recursive_binary_search(list[midpoint+1:], target)
			else:
				return recursive_binary_search(list[:midpoint], target)

def verify2(result):
	print("Target found: ", result)

# result = recursive_binary_search(numbers, 2)
# verify2(result)

###############################
# BINARY SEARCH - STRINGS
# O(log n)
#------------------
from sorting_algs import quick_sort

# Sort names before seach
sorted_names = quick_sort(names)
#!! to output to a file: terminal> python searching_algs.py > sorted.txt 

def binary_search_string(collection, target):
	first = 0
	last= len(collection)
	while first <= last:
		midpt = (first+last)//2
		if collection[midpt] == target:
			return midpt
		elif collection[midpt] < target:
			first = midpt+1
		else:
			last = midpt - 1
	return None

for n in search_names:
	index = binary_search_string(sorted_names, n)
	print(index)

#______________________________________________________________________________________________________________________________________________________
# SLIDING WINDOW
# 
#------------------

def maxSum(values, k):
	n = len(values)
	if n < k:
		print("invalid")
		return -1
	
	window_sum = sum(values[:k])
	max_sum = window_sum
	for i in range(n - k):
		window_sum = window_sum - values[i] + values[i + k]
		max_sum = max(window_sum, max_sum)

	return max_sum

values = [16, 12, 9, 19, 11, 8]
print(maxSum(values, 3))