class MyHashMap:
    def __init__(self):
        self.size = 10
        self.map = [None] * self.size

    def getHashValue(self, key=None):
        hashValue = 0
        for char in key:
            # ord will return numerical value of character
            hashValue += ord(char)
        return hashValue % self.size

    def add(self, key, value):
        hashValue = self.getHashValue(key)
        key_value = [key, value]

        if self.map[hashValue] is None:
            self.map[hashValue] = list([key_value])
            return True
        else:
            for pair in self.map[hashValue]:
                if pair[0] == key:
                    pair[1] = value
                    return True
            self.map[hashValue].append(key_value)
            return True

    def get(self, key):
        hashValue = self.getHashValue(key)
        if self.map[hashValue] is not None:
            for pair in self.map[hashValue]:
                if pair[0] == key:
                    return pair[1]
        return None

    def delete(self, key):
        hashValue = self.getHashValue(key)
        if self.map[hashValue] is None:
            return False
        for i in range(0, len(self.map[hashValue])):
            if self.map[hashValue][i][0] == key:
                self.map[hashValue].pop(i)
                return True

    def printHashMap(self):
        if self.map is not None:
            for item in self.map:
                if item is not None:
                    print(item)
                    print()


if __name__ == "__main__":
    h = MyHashMap()

    h.add('test1', 1)
    h.add('test2', 2)
    h.add('bigstring', 4)
    h.add('test3', 2)
    h.add('test4', 2)
    h.add('test5', 2)
    h.add('test6', 2)
    h.add('test7', 2)
    h.add('test8', 2)
    h.add('test9', 2)
    h.add('test10', 2)
    h.add('test11', 2)
    print('Before delete:')
    h.printHashMap()

    print('After delete:')
    h.delete('test2')
    h.printHashMap()

    print('Get:')
    print(h.get('test1'))