from graph import Graph


def DFS(g, u, discovered):
    discovered[u] = None
    for e in g.incident_edges(u):
        v = e.opposite(u)
        if v not in discovered:
            discovered[v] = e
            DFS(g, v, discovered)
    vertices = discovered.keys()
    elements = []
    for vertex in vertices:
        elements.append(vertex.element())
    return elements


g = Graph()
A = g.insert_vertex('A')
B = g.insert_vertex('B')
C = g.insert_vertex('C')
D = g.insert_vertex('D')
E = g.insert_vertex('E')
g.insert_edge(A, B)
g.insert_edge(A, C)
g.insert_edge(B, D)
g.insert_edge(C, E)

print(DFS(g, A, discovered={}))