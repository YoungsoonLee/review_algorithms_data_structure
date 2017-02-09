import unittest


def countSort(array, maxInt):
	counter = [0] * ( maxInt + 1 )
	for i in array:
		counter[i] += 1
	# print(counter)

	ndx = 0
	for i in range( len( counter ) ):
		# print(i)
		while 0 < counter[i]:			
			array[ndx] = i
			ndx += 1
			counter[i] -= 1
	print(array)


array = [3,4,0,1,2,4,2,4]
countSort(array, 4)

array = [3,4,0,1,6,7]
countSort(array, 7)

array = [54, 6, 645, 67, 3, 5, 7, 856, 898, 9, 657, 57, 1, 567, 2, 0]
countSort(array, 898)

"""
from collections import defaultdict
d = defaultdict(int)
print(d)
for n in range(1, 1001):
	for x in str(n):
		# print(x)
		d[x] += 1
print(d)

test = 123
for x in str(test):
	print(x)
"""

