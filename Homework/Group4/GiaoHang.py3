ans = float('inf') # Minimum time
curTime = 0 # Spent time
visited = [False] * 16 # Check if node is visited
cntVisited = 0 # Number of visited nodes
weight = [[float('inf')] * 16 * 16 for _ in range(16)] # Time to go from u to v
minWeight = [[float('inf')] * 16 * 16 for _ in range(16)] # Minimum time to go from u to v

def solve(i, n): # Go from node i
    global ans, visited, cntVisited, weight, curTime, lastTrace
    if cntVisited == n: # Visited all nodes
        ans = min(ans, curTime)
        return
    if curTime >= ans:
        return
    
    for j in range(2, n+1): # Try to go to node j
        if not visited[j] and weight[i][j] < float('inf'):
            visited[j] = True
            cntVisited += 1
            curTime += weight[i][j]
            solve(j, n) 
            visited[j] = False
            cntVisited -= 1
            curTime -= weight[i][j]

n, m = map(int, input().split())
for i in range(m):
    u, v, w = map(int, input().split())
    weight[u][v] = min(weight[u][v], w)
    weight[v][u] = min(weight[v][u], w)

visited[1] = True
cntVisited = 1
solve(1, n)
if ans < float('inf'):
    print(ans)
else:
    print(-1)