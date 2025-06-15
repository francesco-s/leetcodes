class Solution:
    def searchInsert(self, nums: list[int], target: int) -> int:

        left = 0
        right = len(nums) - 1

        while left <= right:
            middle = (left + right) // 2
            if nums[middle] == target:
                return middle
            elif nums[middle] > target:
                right = middle - 1
            else:
                left = middle + 1

        return left


# Test cases
solution = Solution()

# Test case 1
nums1 = [1, 3, 5, 6]
result1 = solution.searchInsert(nums1, 5)
print(f"Test case 1: {result1}")  # Expected: 2

# Test case 2
nums2 = [1, 3, 5, 6]
result2 = solution.searchInsert(nums2, 2)
print(f"Test case 2: {result2}")  # Expected: 1

# Test case 3
nums3 = [1, 3, 5, 6]
result3 = solution.searchInsert(nums3, 7)
print(f"Test case 3: {result3}")  # Expected: 4

# Test case 4
nums4 = [1, 3, 5, 6]
result4 = solution.searchInsert(nums4, 0)
print(f"Test case 4: {result4}")  # Expected: 0