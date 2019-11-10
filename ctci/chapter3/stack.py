class Stack:
    def __init__(self, size=10):
        self.arr = [None] * size
        self.top = 0

    def push(self, data):
        if self.top < len(self.arr):
            self.arr[self.top] = data
            self.top += 1
        else:
            print("Stack full")

    def pop(self):
        if self.top > 0:
            popped = self.arr[self.top - 1]
            self.arr[self.top - 1] = None
            self.top -= 1
            return popped
        else:
            print("Stack empty")
            return None

    def peek(self):
        if self.top > 0:
            return self.arr[self.top]
        else:
            return -1

    def __repr__(self):
        ret = ''
        if self.top > 0:
            for i in range(self.top):
               ret = ret + str(self.arr[i]) + ' '
            return ret
        else:
            return "Stack empty"

if __name__ == "__main__":
    s = Stack(5)
    s.push(1)
    s.push(2)
    s.push(3)
    s.push(4)
    s.push(5)
    print(s)
    s.push(6)
    print(s.pop())
    print(s.pop())
    print(s)