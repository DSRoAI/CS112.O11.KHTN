# Input
n, S = map(int, input().split())
a = list(map(int, input().split()))

a.sort() # Sắp xếp mệnh giá tăng dần
trace = [] # Lưu cách rút tiền hiện tại
allTrace = []  # Lưu tất cả cách rút tiền hợp lệ

def solve(i, S): # Tìm cách rút S đồng, chỉ rút từ mệnh giá thứ i trở lên
    if S == 0: # Nếu S = 0 thì được 1 cách rút tiền
        allTrace.append(trace.copy())
        return
    for j in range(i, n): # Duyệt qua các mệnh giá thứ i đến n
        if S >= a[j]: # Nếu số tiền cần rút không nhỏ hơn a[j] thì rút 1 tờ a[j]
            trace.append(a[j])
            solve(j, S - a[j])
            trace.pop() # Quay lui, không rút tờ a[j] nữa

solve(0, S) # Bắt đầu rút S đồng, rút từ mệnh giá thứ 0
print(len(allTrace))
for i in allTrace:
    print(*i)