# leetcode 155
class MinStack(object):
    def __init__(self):
        self.data = []
        self.mins = []
        self.minValue = float('-inf')

    def push(self, x):
        if len(self.data) == 0 or x <= self.mins[-1]:
            self.mins += [x]
        self.data += [x]

    def pop(self):
        if len(self.data) <= 0:
            return None
        if self.data[-1] == self.mins[-1]:
            self.mins.pop()
        return self.data.pop()

    def top(self):
        if len(self.data) > 0:
            return self.data[-1]
        else:
            return None

    def getMin(self):
        if len(self.data) > 0:
            return self.mins[-1]
        else:
            return None


minStack = MinStack();
minStack.push(0);
minStack.push(1);
minStack.push(0);
print minStack.getMin();  # --> Returns -3.
minStack.pop();
print minStack.top();  # --> Returns 0.
print minStack.getMin();  # --> Returns -2.
