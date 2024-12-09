from collections import defaultdict
class Graph:
    def __init__(self):
        self.value = defaultdict(list)
    def DrawGraph(self, parent, child):
        self.value[parent].append(child)
    def DFS(self, start):
        visited = [start]
        stack = [start]
        print(start, end = " ")
        while stack:
            s = stack[-1]
            if any(item for item in self.value[s] if item not in visited):
                for item in [item for item in self.value[s] if item not in visited]:
                    stack.append(item)
                    visited.append(item)
                    print(item, end = " ")
                    break
            else:
                stack.pop()
    def BFS(self,start):
        visited = [start]
        queue = [start]
        while queue:
            x = queue.pop(0)
            print(x, end = " ")
            for item in self.value[x]:
                if item not in visited:
                    queue.append(item)
                    visited.append(item)
g = Graph()
g.DrawGraph(1,4)
g.DrawGraph(1,2)
g.DrawGraph(2,3)
g.DrawGraph(2,6)
g.DrawGraph(4,5)
g.DrawGraph(4,7)
g.DrawGraph(7,96)
print("DFS Traversal:")
g.DFS(1)
print("\nBFS Traversal:")
g.BFS(1)
