# assume: all integer

import unittest


def pow(x, n):
    if n == 0:
        return 1
    # negative
    if n < 0:
        return 1 / pow(x, -(n))

    # odd
    if isOdd(n):
        return x * pow(x, n - 1)

    # even
    if isEven(n):
        result = pow(x, int(n / 2))
        return result * result


def isEven(n):
    return int(n % 2) == 0


def isOdd(n):
    return not isEven(n)


class TestPow(unittest.TestCase):
    def test(self):
        self.assertEqual(1, pow(2, 0))
        self.assertEqual(4, pow(2, 2))
        self.assertEqual(1 / 9, pow(3, -2))


if __name__ == '__main__':
    unittest.main()
