a, b, n, x = map(int, input().split())
maxx = max(a, b)
minn = min(a, b)
if maxx >= 0:
    if minn <= 0:
        ans = max(maxx*x, maxx*n + minn*(n-x))
    else:
        ans = maxx*n + minn*n
else:
    ans = 0
print(ans)