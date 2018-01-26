class LRUCache(object):
    def __init__(self, size=5):
        self.size = size
        self.data = {}
        self.index = []

    def get(self, key):
        if self.data.has_key(key):
            self.updateIndex(key)
            return self.data[key]
        else:
            return None

    def updateIndex(self, key):
        if key in self.index:
            self.index.remove(key)
        self.index.insert(0, key)

    def removeOld(self):
        old_key = self.key.pop()
        self.data.pop(old_key)

    def put(self, key, value):
        if self.data.has_key(key):  # if key existed
            self.data[key] = value
        elif len(self.data) == self.size:  # if full
            self.removeOld()
            self.data[key] = value
        else:
            self.data[key] = value
        self.updateIndex(key)

    def getLRU(self):
        return self.index


test = LRUCache()
test.put('a', 1)
test.put('b', 2)
test.put('c', 3)
test.put('d', 4)
test.put('e', 5)
test.put('c', 5)
test.put('b', 5)
print test.getLRU()
print test.get('a')
print test.getLRU()
