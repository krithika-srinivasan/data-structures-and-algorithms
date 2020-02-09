from graph import Graph

def DFS(g, u, discovered):
    for e in g.incident_edges(u):
        v = e.opposite(u)
        if v not in discovered:
            discovered[v] = e
            DFS(g, v, discovered)

def DFS_complete(g):
    forest = {}
    for u in g.vertices():
        if u not in forest:
            forest[u] = None
            DFS(g, u, forest)
    vertices = forest.keys()
    elements = []
    for vertex in vertices:
        elements.append(vertex.element())
    print(elements)
    return forest

def construct_path(u,v, discovered):
    path = []
    if v in discovered:
        path.append(v.element())
        walk = v
        while walk is not u:
            e = discovered[walk]
            parent = e.opposite(walk)
            path.append(parent.element())
            walk = parent
        path.reverse()
    return path


g = Graph()
Root = g.insert_vertex('Root')
A = g.insert_vertex('A')
B = g.insert_vertex('B')
C = g.insert_vertex('C')
D = g.insert_vertex('D')
E = g.insert_vertex('E')
g.insert_edge(Root,A)
g.insert_edge(A, B)
g.insert_edge(A, C)
g.insert_edge(B, D)
g.insert_edge(B, C)
g.insert_edge(C, E)

discovered = DFS_complete(g)
print(discovered)
print(construct_path(B, D, discovered))
