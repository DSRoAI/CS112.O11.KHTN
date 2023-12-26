# Input
n, m = map(int, input().split())
sumL = [0] * m
sumR = [0] * m
for i in range(n):
    l, r, s = map(int, input().split())
    sumL[r - 1] += s
    sumR[l - 1] += s

# sumL[i] = sum satisfaction when only eating on days with plates from [1, i]
for i in range(1, m):
    sumL[i] += sumL[i - 1]

# sumR[i] = sum satisfaction when only eating on days with plates from [i, m]
for i in range(m - 2, -1, -1):
    sumR[i] += sumR[i + 1]

ans = max(sumL[m-2], sumR[1]) # Sum satisfaction when eating on days with plates different from m or 1

# Maximize sum satisfaction when eating on days with plates different i
for i in range(1, m-1):
    ans = max(ans, sumL[i-1] + sumR[i+1])
print(ans)