ans = 0 # So to tien lon nhat
curCnt = 0 # So to tien da tra
trace = [] # Danh sach to tien da tra lon nhat
curTrace = [] # Danh sach to tien da tra
cashes = [] # Danh sach to tien (menh gia, so luong)
def solve(i, n, m): # Xet to tien menh gia thu i, so tien con lai la m
    global ans, trace, curCnt, curTrace
    if m == 0: # Da tra het
        if ans < curCnt: 
            ans = curCnt
            trace = curTrace[:]
        return
    if i == n or m < cashes[i][0]: # Xet het menh gia hoac so tien con lai nho hon menh gia dang xet
        return
    
    # branch and bound, cost function: So to tien da tra + so tien con lai/menh gia tien thu i
    if curCnt + m // cashes[i][0] <= ans:
        return
    
    if cashes[i][1] > 0: # Con to tien menh gia i
        cashes[i] = (cashes[i][0], cashes[i][1] - 1)
        curCnt += 1
        curTrace.append(cashes[i][0])
        solve(i, n, m - cashes[i][0]) # Xet truong hop tra 1 to menh gia i
        curTrace.pop()
        curCnt -= 1
        cashes[i] = (cashes[i][0], cashes[i][1] + 1)
    solve(i + 1, n, m) # Xet truong hop khong tra to menh gia i

n, m = map(int, input().split())
for i in range(n):
    a, b = map(int, input().split())
    cashes.append((a, b))
cashes.sort(key=lambda x: x[0])
solve(0, n, m)
print(ans)
print(*trace)