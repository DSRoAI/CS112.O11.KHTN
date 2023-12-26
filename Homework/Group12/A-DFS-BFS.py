from collections import defaultdict, deque

a = defaultdict(set)  # Adjacency list
visitedDFS = {}       # Check if a vertex is visited in DFS
visitedBFS = {}       # Check if a vertex is visited in BFS

def dfs(s):
    print(s, end=" ")
    visitedDFS[s] = True  # Mark s as visited
    neighbors = a[s]      # Get neighbors of s
    for i in neighbors:
        if i not in visitedDFS:
            dfs(i)  # If i is not visited, call dfs(i)

def bfs(s):
    q = deque([s])
    visitedBFS[s] = True  # Push s to queue and mark s as visited
    while q:
        u = q.popleft()  # Visit the first vertex in the queue
        print(u, end=" ")
        neighbors = a[u]  # Get neighbors of u
        for i in neighbors:
            if i not in visitedBFS:
                q.append(i)  # Push i to queue and mark i as visited
                visitedBFS[i] = True

def reset():
    global a, visitedDFS, visitedBFS
    a = defaultdict(set)
    visitedDFS = {}
    visitedBFS = {}

t = int(input())  # Number of test cases
for _ in range(t):
    reset()
    n = int(input())  # Number of edges
    for _ in range(n):
        u, v = map(int, input().split())  # Edge from u to v
        a[u].add(v)
        a[v].add(u)
    s = int(input())  # Starting vertex
    print("DFS:")
    dfs(s)
    print()
    print("BFS:")
    bfs(s)
    print("\n")