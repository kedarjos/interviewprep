class Queue:
    def __init__(self, size=10):
        self.arr = [None] * size
        self.front = self.rear = 0

    def add(self, data):
        if self.rear < len(self.arr):
            self.arr[self.rear] = data
            self.rear += 1
        else:
            print('Queue full')

    def remove(self):
        if self.front >= 0:
            if self.front < self.rear:
                popped = self.arr[self.front]
                self.arr[self.front] = None
                self.front = self.front + 1
                return popped
            else:
                # Queue is empty so reset
                self.front = self.rear = 0
        else:
            print('Queue empty')

    def __repr__(self):
        rep = ''
        if self.front >= 0:
            for i in range(self.front, self.rear):
                rep = rep + str(self.arr[i]) + ' '
            return rep
        else:
            return 'Queue empty'

if __name__ == "__main__":
    q = Queue(5)
    q.add(1)
    q.add(2)
    q.add(3)
    q.add(4)
    q.add(5)
    print(q)
    q.add(6)
    q.remove()
    q.remove()
    print(q)
