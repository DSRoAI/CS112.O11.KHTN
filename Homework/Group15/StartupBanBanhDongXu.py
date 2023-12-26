n, m = map(int, input().split())
p = [0] * 2005
x = [0] * 2005
disToNearest = [float('inf')] * 2005
maxDis = 0
check = [False] * 1005

def checkSchoolPos(i):
    return i % 100 == 0 and i // 100 + 1 <= n

# Initialize disToNearest with infinity
for i in range(1, n + 1):
    p[i] = int(input())

for i in range(1, m + 1):
    x[i] = int(input())
    check[x[i]] = True
    for j in range(x[i] // 100, n + 1):
        schoolpos = (j - 1) * 100
        if disToNearest[j] > abs(schoolpos - x[i]):
            disToNearest[j] = abs(schoolpos - x[i])

    for j in range(x[i] // 100, 0, -1):
        schoolpos = (j - 1) * 100
        if disToNearest[j] > abs(schoolpos - x[i]):
            disToNearest[j] = abs(schoolpos - x[i])

    maxDis = max(maxDis, x[i])

maxDis += 1
maxCntSold = 0

for i in range(maxDis + 1):
    if checkSchoolPos(i) or check[i]:
        continue

    cntSold = 0

    for j in range(1, n + 1):
        schoolpos = (j - 1) * 100
        if disToNearest[j] >= abs(schoolpos - i):
            cntSold += p[j]

    maxCntSold = max(maxCntSold, cntSold)

print(maxCntSold)

