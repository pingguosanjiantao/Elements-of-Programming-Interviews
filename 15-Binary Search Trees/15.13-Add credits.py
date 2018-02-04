# system design
# not a optimal solution
class ClientsKeyInfo:
    def __init__(self):
        self.offset = 0
        self.clientToKey = {}
        self.keyToClient = {}

    def insert(self, clientID, c):
        self.remove(clientID)
        key = c - self.offset
        self.clientToKey[clientID] = key
        if self.keyToClient.has_key(key):
            self.keyToClient[key] += [clientID]
        else:
            self.keyToClient[key] = [clientID]

    def remove(self, clientID):
        if self.clientToKey.has_key(clientID):
            key = self.clientToKey[clientID]
            if self.keyToClient.has_key(key):
                self.keyToClient[key].remove(clientID)
                if len(self.keyToClient[key]) == 0:
                    del self.keyToClient[key]
            del self.clientToKey[clientID]
            return True
        return False

    def lookup(self, clientID):
        key = self.clientToKey.get(clientID, None)
        return key + self.offset if key is not None else None

    def addAll(self, c):
        self.offset += c

    def max(self):
        maxKey = max(self.keyToClient.keys())
        return self.keyToClient[maxKey][0]
