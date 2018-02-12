# detect a DAG has a cycle, optimal solution
from collections import defaultdict


class Graph:
    def __init__(self):
        self.graph = defaultdict(list)

    def addEdge(self, u, v):
        self.graph[u].append(v)

    def hasCycle(self):
        graph = self.graph
        visited, endVisited = defaultdict(lambda: False), defaultdict(lambda: False)

        def doHasCycle(u):
            if visited[u]:
                return True
            visited[u] = True
            for v in graph[u]:
                if not visited[v] and doHasCycle(v):
                    return True
                elif endVisited[v]:
                    return True
            endVisited[u] = True
            return False

        for u in self.graph:
            if not visited[u] and doHasCycle(u):
                return True
        return False


g = Graph()
g.addEdge(0, 1)
g.addEdge(0, 2)
g.addEdge(1, 2)
g.addEdge(2, 3)
g.addEdge(3, 4)
g.addEdge(4, 2)
print g.hasCycle()
