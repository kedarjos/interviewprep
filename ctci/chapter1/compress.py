# String compression algo
import unittest

def compress(inputString=None):
    if inputString is None:
        return None

    compressed = []
    counter = 0

    for i in range(len(inputString)):
        if i != 0 and inputString[i] != inputString[i - 1]:
            compressed.append(inputString[i - 1] + str(counter))
            counter = 0
        counter += 1

    compressed.append(inputString[-1] + str(counter))

    return min(inputString, ''.join(compressed), key=len)

class CompressTester(unittest.TestCase):
    def testCompression(self):
        self.assertEqual('a3b2c3a2b2', compress('aaabbcccaabb'))

if __name__ == "__main__":
    unittest.main()