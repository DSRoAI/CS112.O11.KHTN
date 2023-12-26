import heapq

a = [[] for _ in range(3005)]  # Adjacency list with pair (vertex, weight)
n = 0  # Number of vertices

def dijkstra(s): # s is the source vertex
    global n
    pq = [] 
    d = [float('inf')] * n  # d[i] is the shortest distance from s to i
    visited = [False] * n  # visited[i] is True if vertex i is visited
    d[s] = 0  # Distance from s to s is 0
    heapq.heappush(pq, (0, s))  # Push s to the queue

    while pq:  # Loop until the queue is empty
        dist_u, u = heapq.heappop(pq)  # Get vertex u with the minimum distance
        if visited[u]:
            continue  # If u is visited, skip
        visited[u] = True
        for v, w in a[u]:  # Loop through all edges of u
            if d[v] > d[u] + w:  # If distance from s to v is greater than distance from s to u plus weight of edge (u, v)
                d[v] = d[u] + w
                heapq.heappush(pq, (d[v], v))  # Push v to the queue

    for i in range(n):
        print(d[i])

n = int(input())
while True:
    u, v, w = map(int, input().split())
    if u == -1:
        break
    a[u].append((v, w))
    a[v].append((u, w))
s = int(input())  # Source vertex
dijkstra(s)