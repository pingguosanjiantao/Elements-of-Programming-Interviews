class Queue:
    def __init__(self, capacity):
        self.head = 0
        self.tail = 0
        self.size = 0
        self.entry = [None] * capacity
        self.SCALE_FACTOR = 1

    def enqueue(self, x):
        if self.size == len(self.entry):
            self.head = 0
            self.tail = self.size
            self.entry += [None] * (self.SCALE_FACTOR * len(self.entry))

        self.entry[self.tail] = x
        self.tail = (self.tail + 1) % len(self.entry)
        self.size += 1

    def dequeue(self):
        if self.size != 0:
            self.size -= 1
            ret = self.entry[self.head]
            self.head = (self.head + 1) % len(self.entry)
            return ret
        return None

    def size(self):
        return self.size


q = Queue(3)
q.enqueue(1)
q.enqueue(2)
q.enqueue(3)
print q.dequeue()
print q.dequeue()
q.enqueue(4)
print q.dequeue()
print q.dequeue()
print q.dequeue()
print q.dequeue()
