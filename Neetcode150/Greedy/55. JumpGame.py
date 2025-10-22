from typing import List


class Solution:
    def canJump(self, nums: List[int]) -> bool:
        max_reach = 0
        for i, num in enumerate(nums):
            if i > max_reach:
                return False
            max_reach = max(max_reach, i + num)
            if max_reach >= len(nums) - 1:
                return True

# Test cases
solution = Solution()

# Test case 1 (example)
nums1 = [2,3,1,1,4]
res1 = solution.canJump(nums1)
print(f"Test case 1: {res1}")  # Expected: True

# Test case 2 (example - stuck at zero)
nums2 = [3,2,1,0,4]
res2 = solution.canJump(nums2)
print(f"Test case 2: {res2}")  # Expected: False

# Test case 3 (single element)
nums3 = [0]
res3 = solution.canJump(nums3)
print(f"Test case 3: {res3}")  # Expected: True

# Test case 4 (all zeros except first)
nums4 = [2,0,0]
res4 = solution.canJump(nums4)
print(f"Test case 4: {res4}")  # Expected: True

# Test case 5 (large jumps)
nums5 = [5,9,3,2,1,0,2,3,3,1,0,0]
res5 = solution.canJump(nums5)
print(f"Test case 5: {res5}")  # Expected: True

# Test case 6 (impossible jump)
nums6 = [1,0,1,0]
res6 = solution.canJump(nums6)
print(f"Test case 6: {res6}")  # Expected: False
