def check(x, n, k, values, weights):
    b = [values[i] - weights[i] * x for i in range(n)]
    b.sort(reverse=True)
    sumv = 0
    for i in range(k):
        sumv += b[i]
        if sumv >= 0:
            continue
        else:
            return False
    return True

def binary_search(n, k, values, weights):
    left = 0
    right = 1e8
    result = 0
    while left <= right:
        mid = (left + right) // 2
        if check(mid, n, k, values, weights):
            left = mid + 1
            result = mid
        else:
            right = mid - 1
    return result

n, k = map(int, input().split())
values = []
weights = []
for i in range(n):
    w, v = map(int, input().split())
    values.append(v)
    weights.append(w)
answer = binary_search(n, k, values, weights)
print(int(answer))