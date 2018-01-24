# Deque is needed
class MaxQueue:
    def __init__(self):
        self.data = []
        self.maxs = []

    def enqueue(self, x):
        while len(self.maxs) > 0:
            if self.maxs[-1] < x:
                self.maxs.pop()
            else:
                break
        self.maxs += [x]
        self.data += [x]

    def dequeue(self):
        if len(self.data) <= 0:
            return None
        if self.data[0] == self.maxs[0]:
            self.maxs.pop(0)
        return self.data.pop(0)

    def max(self):
        return self.maxs[0] if len(self.maxs) > 0 else None


q = MaxQueue()
q.enqueue(1)
print 'max:', q.max()
q.enqueue(3)
print 'max:', q.max()
q.enqueue(2)
print 'max:', q.max()
q.enqueue(1)
print 'max:', q.max()
print q.dequeue()
print 'max:', q.max()
print q.dequeue()
print 'max:', q.max()
print q.dequeue()
print 'max:', q.max()
print q.dequeue()
