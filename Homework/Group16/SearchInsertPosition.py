class Solution:
    def searchInsert(self, nums, target):
        left, right = 0, len(nums) - 1

        while left <= right:
            mid = left + (right - left) // 2

            if nums[mid] == target:
                return mid
            elif nums[mid] < target:
                left = mid + 1
            else:
                right = mid - 1

        return left

def input_target():
    try:
        length = int(input().strip())
        nums = list(map(int, input().strip().split()))
        target = int(input().strip())

        return length, nums, target

    except ValueError:
        print("Invalid input. Please enter valid integers.")
        return None

if __name__ == "__main__":
    length, nums, target = input_target()

    s = Solution()
    print(s.searchInsert(nums, target))
