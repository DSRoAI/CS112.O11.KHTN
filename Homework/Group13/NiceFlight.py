import heapq

def dijkstra(start, dist, graph):
    """
    Perform Dijkstra's algorithm to find the shortest paths from the start node
    to all other nodes in the graph.
    """
    dist[start] = 0
    minHeap = [(0, start)]
    while minHeap:
        d, u = heapq.heappop(minHeap)
        if dist[u] < d:
            continue
        for v, w in graph[u]:
            if dist[u] < float('inf') and dist[v] > dist[u] + w:
                dist[v] = dist[u] + w
                heapq.heappush(minHeap, (dist[v], v))

# Input the number of nodes and edges
n, m = map(int, input().split())

# Initialize adjacency lists for the graph and its reverse
graph = [[] for _ in range(n + 1)]
reverseGraph = [[] for _ in range(n + 1)]

# Store all flights information in a list
allFlights = []

# Input edge information and build the graph
for _ in range(m):
    u, v, w = map(int, input().split())
    graph[u].append((v, w))
    reverseGraph[v].append((u, w))
    allFlights.append((u, v, w))

# Initialize distance arrays for forward and reverse Dijkstra
dist = [float('inf')] * (n + 1)
distReverse = [float('inf')] * (n + 1)

# Run Dijkstra's algorithm on the forward and reverse graphs
dijkstra(1, dist, graph)
dijkstra(n, distReverse, reverseGraph)

# In each flight, try using the voucher for that flight
ans = float('inf')
for u, v, w in allFlights:
    ans = min(ans, dist[u] + w // 2 + distReverse[v]) # Go from 1 to u, use voucher in (u, v), go from v to n

print(ans)