def cross(A, B, C):
    """
    Calculate the cross product of vectors AB and AC.
    """
    return (B[0] - A[0]) * (C[1] - A[1]) - (C[0] - A[0]) * (B[1] - A[1])

def ccw(A, B, C):
    """
    Determine the orientation of three points A, B, and C.
    Returns -1 for clockwise, 0 for collinear, and 1 for counterclockwise.
    """
    S = cross(A, B, C)
    if S < 0:
        return -1
    if S == 0:
        return 0
    return 1

def convex_hull(allWood):
    """
    Compute the convex hull of a set of points.
    """
    arr = []  
    sizeArr = 0
    for wood in allWood:
        while sizeArr >= 2 and ccw(arr[sizeArr - 1], arr[sizeArr - 2], wood) == 1:
            arr.pop()
            sizeArr -= 1
        sizeArr += 1
        arr.append(wood)
    return arr

# Input the number of Pinetrees and Wood
n, m = map(int, input().split())
allPinetree, allWood = [], []

# Input Pinetree coordinates
for i in range(n):
    x, y = map(int, input().split())
    allPinetree.append((x, y))

# Input Wood coordinates
for i in range(m):
    x, y = map(int, input().split())
    allWood.append((x, y))

allWood = sorted(allWood)  # Sort wood by x
L = convex_hull(allWood)
allWood.reverse()
U = convex_hull(allWood)

# Combine Lower and Upper hulls to get the complete convex hull
convexHull = L + U
convexHull = sorted(set(convexHull))  # Remove duplicate points and sort the convex hull

# Print the convex hull points
for wood in convexHull:
    print(wood[0], wood[1])