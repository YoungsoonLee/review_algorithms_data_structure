# -----------------------------------------------------------------------
# O(n^2)
# -----------------------------------------------------------------------


def swap(array, firstIndex, secondIndex):
    temp = array[firstIndex]
    array[firstIndex] = array[secondIndex]
    array[secondIndex] = temp


def indexOfMinimum(array, startIndex):
    minValue = array[startIndex]
    minIndex = startIndex

    for i in range(minIndex, len(array)):
        if array[i] < minValue:
            minValue = array[i]
            minIndex = i
    return minIndex


def selectSort(array):
    for j in range(0, len(array)):
        mIndex = indexOfMinimum(array, j)
        # print(' %r %r , step: %r , array: %r' % (j, mIndex, j, array))
        swap(array, j, mIndex)


if __name__ == '__main__':
    array = [22, 11, 99, 88, 9, 7, 42]
    selectSort(array)
    print(array)
