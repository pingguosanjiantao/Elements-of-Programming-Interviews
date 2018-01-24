class Queue:
    def __init__(self):
        self.stack_in = []
        self.stack_out = []

    def enqueue(self, k):
        self.stack_in += [k]

    def dequeue(self):
        if len(self.stack_out) == 0:
            while len(self.stack_in) > 0:
                self.stack_out += [self.stack_in.pop()]

        if len(self.stack_out) > 0:
            return self.stack_out.pop()
        return None


q = Queue()
q.enqueue(1)
q.enqueue(2)
print q.dequeue()
q.enqueue(3)
print q.dequeue()
q.enqueue(4)
print q.dequeue()
print q.dequeue()
