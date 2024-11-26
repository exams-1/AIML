from collections import defaultdict
class Graph:
    def __init__(self):
        self.value = defaultdict(list)
    def drawGraph(self,parent,child):
        self.value[parent].append(child)
    def DFS(self,start):
        visited = [start]
        stack = [start]
        print(stack,end=" ")
        while stack:
            s = stack[-1]
            if any(item for item in self.value[s] if item not in visited):
                for item in[item for item in self.value[s] if item not in visited]:
                    visited.append(item)
                    stack.append(item)
                    print(stack,end=" ")
                    break
            else:
                stack.pop()
    def BFS(self,start):
        visited = [start]
        queue = [start]
        while queue:
            x = queue.pop(0)
            for item in self.value[x]:
                if item not in visited:
                    queue.append(item)
                    visited.append(item)
g = Graph()
g.drawGraph(1,4)
g.drawGraph(1,2)
g.drawGraph(2,3)
g.drawGraph(2,6)
g.drawGraph(4,5)
g.drawGraph(4,7)
g.drawGraph(7,96)
print("DFS Traversal:")
g.DFS(1)
print("\nBFS Traversal:")
g.BFS(1)
