k = int(input())
c = [int(x) for x in input().split()]
m = int(input())

f = [0] * (m + 1) # f[i] = number of ways to have sum i
f[0] = 1 # no coin is used

c.sort()
for i in range(m+1): # i is the sum
    for j in range(k): # j is the index of the coin
        if c[j] <= i: # if the coin is smaller than the sum
            f[i] += f[i - c[j]] # we can use the coin j to make sum i

print(f[m])
