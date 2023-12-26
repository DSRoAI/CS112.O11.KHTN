S = input() # Dãy ngoặc ban đầu
len_S = len(S) # Độ dài dãy ngoặc ban đầu
curS = [] # Dãy ngoặc hiện tại (sau khi đã xóa vài kí tự)
trace = [] # Dãy ngoặc đúng (xóa ít kí tự nhất)
ans = 0 # Độ dài của dãy ngoặc đúng (xóa ít kí tự nhất)

# Kiểm tra dãy ngoặc hiện tại có hợp lệ hay không
def correct():
  cnt = 0
  for i in range(len(curS)):
      if curS[i] == "(":
        cnt += 1
      else:
        cnt -= 1
      if cnt < 0:
        return False
  return cnt == 0

# So sánh thứ tự từ điển giữa dãy ngoặc hiện tại và dãy ngoặc tốt nhất trước đó
# Trả về True nếu dãy ngoặc hiện tại có thứ tự từ điển nhỏ hơn
def compare():
  for i in range(len(curS)):
    if curS[i] == trace[i]:
      continue
    return curS[i] < trace[i]
  return False
  
# Hàm quay lui, xét kí tự thứ i
def solve(i):
    global ans, trace
    if i == len_S:
        if correct():
          if ans < len(curS) or (ans == len(curS) and compare()): 
            ans = len(curS)
            trace = curS.copy()
        return
    # Không xóa kí tự thứ i
    curS.append(S[i])
    solve(i + 1)

    # Xóa kí tự thứ i
    curS.pop()
    solve(i + 1)

solve(0)
print(ans)
for i in trace:
    print(i, end='')