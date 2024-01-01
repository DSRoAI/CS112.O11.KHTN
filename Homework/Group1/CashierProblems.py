k = int(input())
c = [int(x) for x in input().split()]
m = int(input())

f = [21062000004] * (m + 1) # f[i] = minimum number of coins to make sum i
f[0] = 0 # no coin is used

c.sort()
for i in range(m+1): # i is the sum
    for j in range(k): # j is the index of the coin
        if c[j] <= i: # if the coin is smaller than the sum
            f[i] = min(f[i], f[i - c[j]] + 1) # we can use the coin j to make sum i

print(f[m] if f[m] != 21062000004 else -1)
