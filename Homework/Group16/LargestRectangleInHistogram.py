class Solution:
    def largestRectangleArea(self, heights) -> int:
        max_area = 0
        stack = []

        def calculate_area(index, height):
            nonlocal max_area
            start = index
            
            while stack and stack[-1][1] > height:
                popped_index, popped_height = stack.pop()
                max_area = max(max_area, (index - popped_index) * popped_height)
                start = popped_index
            
            stack.append((start, height))

        for index, height in enumerate(heights):
            calculate_area(index, height)

        while stack:
            popped_index, popped_height = stack.pop()
            max_area = max(max_area, (len(heights) - popped_index) * popped_height)

        return max_area

if __name__ == "__main__":
    s = Solution()
    heights = [int(x) for x in input().split()]
    print(s.largestRectangleArea(heights))
