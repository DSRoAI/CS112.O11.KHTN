edges = []  # All edges of the graph
par = []    # Parent of each vertex in DSU

def root(u):
    # Find the root of u in DSU
    if par[u] < 0:
        return u
    par[u] = root(par[u])
    return par[u]

def connect(u, v):
    # Connect u and v in DSU
    u = root(u)
    v = root(v)
    if u == v:
        return
    if par[u] > par[v]:
        u, v = v, u
    par[u] += par[v]
    par[v] = u

def kruskal():
    # Kruskal's algorithm
    edges.sort()  # Sort edges by weight
    cost = 0      # Total cost of MST
    for w, (u, v) in edges:
        if root(u) != root(v):  # If u and v are not connected
            cost += w            # Add edge (u, v) to MST
            connect(u, v)        # Connect u and v
    print(cost)

n = int(input())
par = [-1] * n
while True:
    u, v, w = map(int, input().split())
    if u == -1:
        break
    edges.append((w, (u, v)))
kruskal()