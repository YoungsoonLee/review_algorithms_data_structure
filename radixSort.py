import unittest
from collections import defaultdict

"""
	radix is Maximum number of digits
"""
def radixsort( aList):
	RADIX = 10  # init radix
	maxLength = False
	tmp , placement = -1, 1
 
	while not maxLength:
		maxLength = True
		# declare and initialize buckets
		buckets = [list() for _ in range( RADIX )]
		# print(buckets)

		# split aList between lists
		for  i in aList:
			tmp = i / placement
			# print(int(tmp))
			buckets[ int(tmp % RADIX) ].append( i )
			if maxLength and tmp > 0:
				maxLength = False
		# empty lists into aList array
		a = 0
		for b in range( RADIX ):
			buck = buckets[b]
			for i in buck:
				aList[a] = i
				a += 1 
		# move to next digit
		placement *= RADIX 

array = [125,383,274,96,0,9,81,72]
radixsort(array);
print(array)


		



