def binarySearch(arrays, item):
    # print(isinstance(arrays, list))
    if isinstance(arrays, list) is False:
        return 'not array'
    else:
        min = 0
        max = len(arrays) - 1

        while min <= max:
            guess = int((min + max) / 2)

            # print(guess)
            # print(arrays[guess])

            if arrays[guess] == item:
                return 'there is %r.' % guess
            if arrays[guess] < item:
                min = guess + 1
            elif arrays[guess] > item:
                max = guess - 1

        return 'no item'


if __name__ == '__main__':
    primes = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37,
              41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97]
    print(binarySearch(primes, 11))
