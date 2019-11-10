import unittest

# Time complexity: O(n)
# Space complexity: O(n)
def isUnique(str=None):
    mydict = {}
    for c in str:
        if c in mydict:
            return False
        else:
            mydict[c] = True
    return True

# Time complexity: O(n)
# Space complexity: O(1)
def isUnique2(str=None):
    # Assuming ASCII characters
    char_set = [False for _ in range(128)]
    for c in str:
        val = ord(c)
        if char_set[val]:
            return False
        else:
            char_set[val] = True
    return True

class TestUniquechar(unittest.TestCase):
    def tests(self):
        self.assertTrue(isUnique('kedar'))
        self.assertFalse(isUnique('aaaa'))

        # 2nd function
        self.assertTrue(isUnique2('kedar'))
        self.assertFalse(isUnique2('aaaa'))

if __name__ == "__main__":
    unittest.main()