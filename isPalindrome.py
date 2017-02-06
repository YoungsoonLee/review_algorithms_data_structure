# -----------------------------------------------------------------------
# O(n^2)
# -----------------------------------------------------------------------
import unittest


def isPalindrome(str):
    if len(str) <= 1:
        return True

    if((str[0]) != (str[-1])):
        return False

    return isPalindrome(str[1:-1])


class testIsPalindrome(unittest.TestCase):

    def test(self):
        self.assertEqual(isPalindrome('a'), True)
        self.assertEqual(isPalindrome('ab'), False)
        self.assertEqual(isPalindrome('motor'), False)
        self.assertEqual(isPalindrome('rotor'), True)

if __name__ == '__main__':
    unittest.main()
