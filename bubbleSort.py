import unittest


def bubbleSort(array):
	for i in range(0,len(array)-1):
		for j in range(0, len(array)-1):
			if array[j]  > array[j+1]:
				temp = array[j]
				array[j] = array[j+1]
				array[j+1] = temp
	print(array)
	return array


class Test(unittest.TestCase):
	def test(self):
		self.assertEqual(bubbleSort([5,1,7,4,6,3,2,8]), [1,2,3,4,5,6,7,8])


if __name__ == '__main__':
	unittest.main()

