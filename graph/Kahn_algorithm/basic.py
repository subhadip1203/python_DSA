'''
Link : https://www.youtube.com/watch?v=hM7-4viROWo

Topological sorting for Directed Acyclic Graph (DAG)
'''

from collections import deque

class Graph:
 
    # Constructor
    def __init__(self, edges, N):
 
        # A list of lists to represent an adjacency list
        self.adjList = [[] for _ in range(N)]
 
        # initialize indegree of each vertex by 0
        self.indegree = [0] * N
 
        # add edges to the undirected graph
        for (src, dest) in edges:
 
            # add an edge from source to destination
            self.adjList[src].append(dest)
 
            # increment in-degree of destination vertex by 1
            self.indegree[dest] = self.indegree[dest] + 1

        # print(self.adjList)
        # print(self.indegree)

def doTopologicalSort(graph, N):
    # list to store the sorted elements
    L = []
    # get in-degree information of the graph
    indegree = graph.indegree
    # Set of all nodes with no incoming edges
    S = deque([i for i in range(N) if indegree[i] == 0])

    while S:
 
        # remove node `n` from `S`
        n = S.pop()
 
        # add `n` at the tail of `L`
        L.append(n)
 
        for m in graph.adjList[n]:
 
            # remove an edge from `n` to `m` from the graph
            indegree[m] = indegree[m] - 1
 
            # if `m` has no other incoming edges, insert `m` into `S`
            if indegree[m] == 0:
                S.append(m)
 
    # if a graph has edges, then the graph has at least one cycle
    for i in range(N):
        if indegree[i]:
            return None
 
    return L

edges = [(0, 6), (1, 2), (1, 4), (1, 6), (3, 0), (3, 4), (5, 1), (7, 0), (7, 1)]
N = 8
graph = Graph(edges, N)
L = doTopologicalSort(graph, N)
if L:
    print(L)
else:
    print("Graph has at least one cycle. Topological sorting is not possible.")