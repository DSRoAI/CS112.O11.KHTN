class Solution:
    def computeArea(self, ax1: int, ay1: int, ax2: int, ay2: int, bx1: int, by1: int, bx2: int, by2: int) -> int:
        def calculate_overlap(coord1, coord2):
            return max(0, min(coord1[1], coord2[1]) - max(coord1[0], coord2[0]))

        def calculate_area(coord):
            return abs(coord[2] - coord[0]) * abs(coord[3] - coord[1])

        x_overlap = calculate_overlap((ax1, ax2), (bx1, bx2))
        y_overlap = calculate_overlap((ay1, ay2), (by1, by2))

        overlap_area = x_overlap * y_overlap
        total_area = calculate_area((ax1, ay1, ax2, ay2)) + calculate_area((bx1, by1, bx2, by2))

        return total_area - overlap_area

if __name__ == "__main__":
    coordinates = [int(x) for x in input().split()]
    s = Solution()
    print(s.computeArea(*coordinates))
