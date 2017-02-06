# -----------------------------------------------------------------------
#  O(n^2)
# -----------------------------------------------------------------------


def insertionSort(args):
    for index in range(1, len(args)):
        currentValue = args[index]
        postion = index

        while postion > 0 and args[postion - 1] > currentValue:
            args[postion] = args[postion - 1]
            postion = postion - 1

        args[postion] = currentValue

    return args

l = [5, 6, 1, 2, 4, 3, -3, 0]
print(insertionSort(l))
