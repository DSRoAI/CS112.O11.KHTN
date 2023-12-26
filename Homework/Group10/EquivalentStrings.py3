import math

def distance(Array: list, i: int, j: int):
    return math.sqrt((Array[i][0] - Array[j][0]) ** 2 + (Array[i][1] - Array[j][1]) ** 2)

N = int(input())

Array = []
for _ in range(N):
    x, y = map(int, input().split())
    Array.append((x, y))

min_distance = float('inf')
for i in range(N):
    for j in range(i + 1, N):
        if (min_distance > distance(Array, i, j)):
            min_distance = distance(Array, i, j)

print(min_distance)