from graph import Graph


def BFS(g, s, discovered):
    level = [s]
    while len(level) > 0:
        next_level = []
        for u in level:
            for e in g.incident_edges(u):
                v = e.opposite(u)
                if v not in discovered:
                    discovered[v] = e
                    next_level.append(v)
        level = next_level


def BFS_complete(g):
    forest = {}
    for u in g.vertices():
        if u not in forest:
            forest[u] = None
            BFS(g, u, forest)

    vertices = forest.keys()
    elements = []
    for vertex in vertices:
        elements.append(vertex.element())
    print(elements)
    return forest


g = Graph()
Root = g.insert_vertex('Root')
A = g.insert_vertex('A')
B = g.insert_vertex('B')
C = g.insert_vertex('C')
D = g.insert_vertex('D')
E = g.insert_vertex('E')
g.insert_edge(Root, A)
g.insert_edge(A, B)
g.insert_edge(A, C)
g.insert_edge(B, D)
g.insert_edge(B, C)
g.insert_edge(C, E)

BFS_complete(g)
