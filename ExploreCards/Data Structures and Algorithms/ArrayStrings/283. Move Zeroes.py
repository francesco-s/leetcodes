from typing import List

# LeetCode Problem 283: Move Zeroes
# https://leetcode.com/problems/move-zeroes/


class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        i, j = 0, 0

        while i < len(nums):
            if nums[i] == 0:
                i += 1
            else:
                nums[i], nums[j] = nums[j], nums[i]
                j += 1
                i += 1
        

# Test cases
solution = Solution()

# Test case 1
nums1 = [0, 1, 0, 3, 12]
solution.moveZeroes(nums1)
print(f"Test case 1: {nums1}")  # Expected: [1, 3, 12, 0, 0]

# Test case 2
nums2 = [0, 0, 1]
solution.moveZeroes(nums2)
print(f"Test case 2: {nums2}")  # Expected: [1, 0, 0]

# Test case 3
nums3 = [1, 0, 2, 0, 3]
solution.moveZeroes(nums3)
print(f"Test case 3: {nums3}")  # Expected: [1, 2, 3, 0, 0]

# Test case 4
nums4 = [0, 0, 0]
solution.moveZeroes(nums4)
print(f"Test case 4: {nums4}")  # Expected: [0, 0, 0]

# Test case 5
nums5 = [1, 2, 3]
solution.moveZeroes(nums5)
print(f"Test case 5: {nums5}")  # Expected: [1, 2, 3]