n = int(input())
a = []
for i in range(n):
    s, e = map(int, input().split())
    a.append((s, e))
a = sorted(a, key=lambda x: x[1])
last = 0
ans = 0
for i in range(n):
    if a[i][0] >= last:
        ans += 1
        last = a[i][1]
print(ans)