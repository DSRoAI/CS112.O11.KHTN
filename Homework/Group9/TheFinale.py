def crossProductOrientation(a, b, c):
    f = (b[0] - a[0]) * (b[1] + a[1]) + (c[0] - b[0]) * (c[1] + b[1]) + (a[0] - c[0]) * (a[1] + c[1])
    if f > 0:
        return "RIGHT"
    elif f < 0:
        return "LEFT"
    return "TOUCH"

n = int(input())
for i in range(n):
    x0, y0, x1, y1, x2, y2 = map(int, input().split())
    a = (x0, y0)
    b = (x1, y1)
    c = (x2, y2)
    print(crossProductOrientation(a, b, c))