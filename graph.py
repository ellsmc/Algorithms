
class Vertex:
    """
    Allows for storage of connecting vertices with a dict, and edge adjustment
    """
    def __init__(self, value) -> None:
        self.value = value
        self.edges = {}
    def add_edge(self, vertex, weight = 0):
        pass
    def get_edges(self):
        pass

class Graph_Vertex:
    def __init__(self) -> None:
        pass
    def add_vertex(self, vertex):
        pass
    def add_edge(self, from_vertex, to_vertex, weight = 0):
        pass
    def find_path(self, start_vertex, end_vertex):
        pass
########################################################
# Time complexity: O(V + E), where V is the number of vertices and E is the number of edges in the graph.
# uxiliary Space: O(V + E), since an extra visited array of size V is required, And stack size for iterative call to DFS function.

from collections import defaultdict
# Defaultdict is a container, sub-class of the dictionary class that returns a dictionary-like object.
# defaultdict(<class 'list'>, {0: [0], 1: [1], 2: [2], 3: [3], 4: [4]})

class Graph:
    def __init__(self) -> None:
        self.graph = defaultdict(list)
    
    def add_edge(self, u, v):
        self.graph[u].append(v)
    
    def DFSUtil(self, v, visited):
        # Mark node as visited and print it
        visited.add(v)
        print(v, end=" ")

        # Recursively for all adjacent vertices
        for neighbour in self.graph[v]:
            if neighbour not in visited:
                self.DFSUtil(neighbour, visited)
    
    def DFS(self, v):
        # Set items are unordered, unchangeable, and do not allow duplicate values.
        # ***items can appear in a different order every time you use them, and cannot be referred to by index or key.
        visited = set()
        self.DFSUtil(v, visited)

g = Graph()
g.add_edge(0, 1)
g.add_edge(0, 2)
g.add_edge(1, 2)
g.add_edge(2, 0)
g.add_edge(2, 3)
g.add_edge(3, 3)

print("Following is Depth First Traversal (starting from vertex 2)")
# Function call
g.DFS(2)