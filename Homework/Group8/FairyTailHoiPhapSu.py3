n = int(input())
a = []
for i in range(n):
    t, d = map(int, input().split())
    a.append((t, d))
a = sorted(a, key=lambda x: (x[0], -x[1]))
sumTime = 0
ans = 0
for i in range(n):
    sumTime += a[i][0]
    ans += a[i][1] - sumTime
print(ans)