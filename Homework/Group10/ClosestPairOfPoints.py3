def compare(a: str, b: str):
    if (len(a) != len(b)):
        return False
    else:
        if (len(a) % 2 == 1):
            return (a == b)
        else:
            mid = int(len(a) / 2)
            return (compare(a[ : mid], b[ : mid]) and compare(a[mid : ], b[mid : ])) or (compare(a[ : mid], b[mid : ]) and compare(a[mid : ], b[ : mid]))

a = str(input()).strip()
b = str(input()).strip()

if (compare(a, b)):
    print('YES')
else:
    print('NO')