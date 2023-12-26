def onSegmentCheck(x0, y0, x1, y1, x2, y2):
    # Check if point (x2, y2) lies on the line segment defined by (x0, y0) and (x1, y1)
    return min(x0, x1) <= x2 <= max(x0, x1) and min(y0, y1) <= y2 <= max(y0, y1)

def orientation(x0, y0, x1, y1, x2, y2):
    # Determine the orientation of point (x2, y2) with respect to the line segment defined by (x0, y0) and (x1, y1)
    val = (y1 - y0) * (x2 - x1) - (x1 - x0) * (y2 - y1)
    return 0 if val == 0 else 1 if val > 0 else 2

def solve(x0, y0, x1, y1, x2, y2, x3, y3):
    # Calculate orientations for all relevant pairs of points
    o1, o2, o3, o4 = orientation(x0, y0, x1, y1, x2, y2), orientation(x0, y0, x1, y1, x3, y3), orientation(x2, y2, x3, y3, x0, y0), orientation(x2, y2, x3, y3, x1, y1)

    # Check for general intersection
    if o1 != o2 and o3 != o4:
        return True

    # Check for special cases when points are collinear
    if o1 == 0 and onSegmentCheck(x0, y0, x1, y1, x2, y2):
        return True
    if o2 == 0 and onSegmentCheck(x0, y0, x1, y1, x3, y3):
        return True
    if o3 == 0 and onSegmentCheck(x2, y2, x3, y3, x0, y0):
        return True
    return o4 == 0 and onSegmentCheck(x2, y2, x3, y3, x1, y1)

t = int(input())
for _ in range(t):
    x0, y0, x1, y1, x2, y2, x3, y3 = map(int, input().split())
    print("YES" if solve(x0, y0, x1, y1, x2, y2, x3, y3) else "NO")