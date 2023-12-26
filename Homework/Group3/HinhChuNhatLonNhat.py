def countOneInRange(i, j, z, k):
    global sum_matrix
    # So luong so 1 trong hinh chu nhat co goc trai tren la (i, j), goc phai duoi laf (z, k)
    return sum_matrix[z][k] - sum_matrix[z][j-1] - sum_matrix[i-1][k] + sum_matrix[i-1][j-1]

m, n = map(int, input().split())
a = [[0] * (m+1) for _ in range(n+1)]  # Ma tran ban dau
sum_matrix = [[0] * (m+1) for _ in range(n+1)]  # sum[i][j] = so luong so 1 trong hinh chu nhat co goc trai tren la (1, 1), goc phai duoi la (i, j)

for i in range(1, n + 1):
    a[i][1:m+1] = map(int, input().split())

for i in range(1, n + 1):
    for j in range(1, m + 1):
        sum_matrix[i][j] = sum_matrix[i-1][j] + sum_matrix[i][j-1] - sum_matrix[i-1][j-1]
        if a[i][j] == 1:
            sum_matrix[i][j] += 1

ans = 0
# Chon hinh chu nhat voi goc trai tren la (i, j) va goc phai duoi la (z, k)
for i in range(1, n + 1):
    for j in range(1, m + 1):
        if a[i][j] != 1:
            continue
        for z in range(i, n + 1):
            for k in range(j, m + 1):
                if a[z][k] != 1:
                    continue
                cntCell = (j - i + 1) * (k - z + 1)
                if cntCell != countOneInRange(i, j, z, k):
                    continue
                ans = max(ans, cntCell)  # Neu so luong so 1 = so luong o trong hcn thi update ans

print(ans)