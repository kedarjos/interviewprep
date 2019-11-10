import unittest
from collections import Counter

# Time Complexity: O(nlog(n))
# Space complexity: O(n)
def isPermutation(str1=None, str2=None):
    if len(str1) != len(str2):
        return False

    sorted1 = sorted(str1)
    sorted2 = sorted(str2)
   
    for char1, char2 in zip(sorted1, sorted2):
        if char1 != char2:
            return False
    
    return True

# Time complexity: O(n)
# Space complexity: O(1)
def isPermutation2(str1=None, str2=None):
    if len(str1) != len(str2):
        return False

    counter = Counter()
    for c in str1:
        counter[c] += 1
    for c in str2:
        if counter[c] == 0:
            return False
        counter[c] -= 1
    return True

class TestPermutations(unittest.TestCase):
    def testIfPermutations(self):
        self.assertTrue(isPermutation('test1', '1estt'))
        self.assertTrue(isPermutation('abcd', 'bacd'))
        self.assertTrue(isPermutation('3563476', '7334566'))
        self.assertTrue(isPermutation('wef34f', 'wffe34'))
        self.assertFalse(isPermutation('test1', '2estt'))
        self.assertFalse(isPermutation('abcd', 'd2cba'))
        self.assertFalse(isPermutation('2354', '1234'))
        self.assertFalse(isPermutation('dcw4f', 'dcw5f'))

    def testIfPermutations2(self):
        self.assertTrue(isPermutation2('test1', '1estt'))
        self.assertTrue(isPermutation2('abcd', 'bacd'))
        self.assertTrue(isPermutation2('3563476', '7334566'))
        self.assertTrue(isPermutation2('wef34f', 'wffe34'))
        self.assertFalse(isPermutation2('test1', '2estt'))
        self.assertFalse(isPermutation2('abcd', 'd2cba'))
        self.assertFalse(isPermutation2('2354', '1234'))
        self.assertFalse(isPermutation2('dcw4f', 'dcw5f'))

if __name__ == "__main__":
    unittest.main()