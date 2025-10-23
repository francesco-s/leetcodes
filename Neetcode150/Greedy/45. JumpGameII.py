from typing import List


class Solution:
    def jump(self, nums: List[int]) -> int:
        max_reach = 0
        times = 0
        current_end = 0

        if len(nums) == 1:
            return 0

        for i, num in enumerate(nums):
            if max_reach < i + num:
                max_reach = i + num
            
            if i == current_end:
                times += 1
                current_end = max_reach

                if max_reach >= len(nums) - 1:
                    return times


# Test cases
solution = Solution()

# Test case 1 (example)
nums1 = [2,3,1,1,4]
res1 = solution.jump(nums1)
print(f"Test case 1: {res1}")  # Expected: 2

# Test case 2 (example)
nums2 = [2,3,0,1,4]
res2 = solution.jump(nums2)
print(f"Test case 2: {res2}")  # Expected: 2

# Test case 3 (single element)
nums3 = [0]
res3 = solution.jump(nums3)
print(f"Test case 3: {res3}")  # Expected: 0

# Test case 4 (already at end)
nums4 = [1]
res4 = solution.jump(nums4)
print(f"Test case 4: {res4}")  # Expected: 0

# Test case 5 (large jumps)
nums5 = [5,9,3,2,1,0,2,3,3,1,0,0]
res5 = solution.jump(nums5)
print(f"Test case 5: {res5}")  # Expected: 3

# Test case 6 (multiple jumps needed)
nums6 = [1,1,1,1,1]
res6 = solution.jump(nums6)
print(f"Test case 6: {res6}")  # Expected: 4
