# LeetCode 217: Contains Duplicate
# https://leetcode.com/problems/contains-duplicate/

from collections import defaultdict


class Solution:
    def containsDuplicate(self, nums):
        counter = defaultdict(int)

        for num in nums:
            counter[num] += 1
            if counter[num] > 1:
                return True
            
        return False

# Test cases
solution = Solution()

# Test case 1
nums1 = [1, 2, 3, 1]
print(f"Test case 1: {solution.containsDuplicate(nums1)}")  # Expected: True

# Test case 2
nums2 = [1, 2, 3, 4]
print(f"Test case 2: {solution.containsDuplicate(nums2)}")  # Expected: False

# Test case 3
nums3 = [1, 1, 1, 3, 3, 4, 3, 2, 4, 2]
print(f"Test case 3: {solution.containsDuplicate(nums3)}")  # Expected: True

# Test case 4
nums4 = []
print(f"Test case 4: {solution.containsDuplicate(nums4)}")  # Expected: False

# Test case 5
nums5 = [99]
print(f"Test case 5: {solution.containsDuplicate(nums5)}")  # Expected: False
