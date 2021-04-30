"""
Graph is a data structure that consists of following two components:
1. A finite set of vertices also called as nodes.
2. A finite set of ordered pair of the form (u, v) called as edge. The pair is ordered because (u, v) is not same as (v, u) in case of directed graph(di-graph). The pair of form (u, v) indicates that there is an edge from vertex u to vertex v. The edges may contain weight/value/cost.
Graphs can be represented by two ways:
1. Adjacency Matrix: A two-dimensional matrix, in which the rows represent source vertices and columns represent destination vertices. Data on edges and vertices must be stored externally. Only the cost for one edge can be stored between each pair of vertices.
2. Adjacency List: Vertices are stored as records or objects, and every vertex stores a list of adjacent vertices. This data structure allows the storage of additional data on the vertices. Additional data can be stored if edges are also stored as objects, in which case each vertex stores its incident edges and each edge stores its incident vertices.

TIME COMPLEXITY

Store Graph: AL: O(|V| + |E|), AM: O(|V| * |V|)
Add Vertex: AL: O(1), AM: O(|V| * |V|)
Add Edge: AL: O(1), AM: O(1)
Remove Vertex: AL: O(|E|), AM: O(|V| * |V|)
Remove Edge: AL: O(|V|), AM: O(1)

AL: Slow to remove vertices and edges, because it needs to find all vertices or edges
AM: Slow to add or remove vertices, because matrix must be resized/copied
"""
class AdjacencyList(object):
    def __init__(self):
        self.List = {}
    
    def addEdge(self, fromVertex, toVertex):
        # check if vertex is already present
        if fromVertex in self.List.keys():
            self.List[fromVertex].append(toVertex)
        else:
            self.List[fromVertex] = [toVertex]
    
    def printList(self):
        for i  in self.List:
            print(i,'->',' -> '.join([str(j) for j in self.List[i]]))
            
al = AdjacencyList()
al.addEdge(0, 1)
al.addEdge(0, 4)
al.addEdge(4, 1)
al.addEdge(4, 3)
al.addEdge(1, 0)
al.addEdge(1, 4)
al.addEdge(1, 3)
al.addEdge(1, 2)
al.addEdge(2, 3)
al.addEdge(3, 4)

al.printList()

#OUTPUT:-
# 0 -> 1 -> 4
# 1 -> 0 -> 4 -> 3 -> 2
# 2 -> 3
# 3 -> 4
# 4 -> 1 -> 3