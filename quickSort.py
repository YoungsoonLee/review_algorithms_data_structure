import unittest

# return pivot index
def partition(array, left, right, pivotIndex):	
	pivot = array[pivotIndex] # right is pivot
	while left <= right:
		while array[left] < pivot:
			left += 1
		while array[right] > pivot:
			right -= 1

		if left <= right:
			temp = array[left]
			array[left] = array[right]
			array[right] = temp
			left += 1
			right -= 1
	temp = array[left]
	array[left] = array[pivotIndex]
	array[pivotIndex] = temp
	return left

def quickSort(array, left, right):
	# if left is None: left = 0
	# if right is None: right = len(array) - 1
	
	pivotIndex = right
	pivotIndex = partition(array, left, right-1, pivotIndex)
	if left < pivotIndex -1:
		quickSort(array, left, pivotIndex-1)
	if right > pivotIndex +1:
		quickSort(array, pivotIndex+1, right)
	return array

class Test(unittest.TestCase):
	def test(self):
		array = [4,1,7,6,3,8,2,5]
		self.assertEqual(quickSort(array, 0, len(array)-1), [1,2,3,4,5,6,7,8])


if __name__ == '__main__':
	unittest.main()


