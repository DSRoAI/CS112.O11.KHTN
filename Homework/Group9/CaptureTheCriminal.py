def crossProductOrientation(a, b, c):
    """
    Calculate the cross product orientation of three points (a, b, c).
    The result indicates the direction of the cross product:
    1 - Clockwise orientation
   -1 - Counterclockwise orientation
    0 - Collinear orientation
    """
    f = (b[0] - a[0]) * (b[1] + a[1]) + (c[0] - b[0]) * (c[1] + b[1]) + (a[0] - c[0]) * (a[1] + c[1])
    if f > 0:
        return 1
    elif f < 0:
        return -1
    return 0

def pointOnSegment(a, b, c):
    """
    Check if point 'a' lies on the line segment defined by points 'b' and 'c'.
    """
    return min(b[0], c[0]) <= a[0] <= max(b[0], c[0]) and min(b[1], c[1]) <= a[1] <= max(b[1], c[1])

def pointLocation(polygon, point):
    """
    Determine the location of a point relative to a polygon:
    - "BOUNDARY" if the point lies on the boundary of the polygon,
    - "INSIDE" if the point is inside the polygon,
    - "OUTSIDE" if the point is outside the polygon.
    """
    n = len(polygon) - 1
    is_boundary = False
    intersection_count = 0

    for i in range(n):
        orientation_result = crossProductOrientation(point, polygon[i], polygon[i + 1])
        if orientation_result == 0 and pointOnSegment(point, polygon[i], polygon[i + 1]):
            is_boundary = True
            break
        if polygon[i][0] <= point[0] < polygon[i + 1][0] and crossProductOrientation(polygon[i], polygon[i + 1], point) > 0:
            intersection_count += 1
        elif polygon[i + 1][0] <= point[0] < polygon[i][0] and crossProductOrientation(polygon[i + 1], polygon[i], point) > 0:
            intersection_count += 1

    if is_boundary:
        return "BOUNDARY"
    elif intersection_count % 2 == 1:
        return "INSIDE"
    else:
        return "OUTSIDE"

# Input
n, m = map(int, input().split())
polygon = [tuple(map(int, input().split())) for _ in range(n)]
polygon.append(polygon[0])

# Process and output
for _ in range(m):
    x, y = map(int, input().split())
    result = pointLocation(polygon, (x, y))
    print(result)