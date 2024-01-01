a, b, c, d = input().split()
a = int(a)
b = int(b)
c = int(c)
d = int(d)
if b <= c or d <= a: # Two segments do not intersect
    print(0)
else:
    print(min(b, d) - max(a, c))
