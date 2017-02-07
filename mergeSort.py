
# ---------------------------------------------------
#  not use Python list sort
# ---------------------------------------------------

import unittest

def mergeSort(array):
	if len(array) < 2: return array
	mid = int(len(array) / 2)
	lowHalf = array[0:mid]	
	highHalf = array[mid:len(array)]
	return merge(mergeSort(lowHalf), mergeSort(highHalf))


def merge(lowHalf, highHalf):
	result = list()	
	while len(lowHalf) and len(highHalf):
		if lowHalf[0] < highHalf[0]:
			result.append(lowHalf.pop(0))
		else:
			result.append(highHalf.pop(0))

	while lowHalf:
		result.append(lowHalf.pop(0))

	while highHalf:
		result.append(highHalf.pop(0))
		
	return result		


class Test(unittest.TestCase):
	def test(self):
		self.assertEqual(mergeSort([5,2,4,7,6,1,3,8]), [1, 2, 3, 4, 5, 6, 7, 8])
		self.assertEqual(mergeSort([5,2,4,7,6,1,3,8,0,-2]), [-2,0,1, 2, 3, 4, 5, 6, 7, 8])


if __name__ == '__main__':
	unittest.main()