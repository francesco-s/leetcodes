# LeetCode 1: Two Sum
# https://leetcode.com/problems/two-sum/

class Solution:
    def twoSum(self, nums, target):
        complements = {}

        for i, num in enumerate(nums):
            complement = target - num
            if complement in complements:
                return [complements[complement], i]
            complements[num] = i
            



# Test cases
solution = Solution()

# Test case 1
nums1 = [2, 7, 11, 15]
target1 = 9
print(f"Test case 1: {solution.twoSum(nums1, target1)}")  # Expected: [0, 1]

# Test case 2
nums2 = [3, 2, 4]
target2 = 6
print(f"Test case 2: {solution.twoSum(nums2, target2)}")  # Expected: [1, 2]

# Test case 3
nums3 = [3, 3]
target3 = 6
print(f"Test case 3: {solution.twoSum(nums3, target3)}")  # Expected: [0, 1]

# Test case 4
nums4 = [1, 5, 7, 9]
target4 = 14
print(f"Test case 4: {solution.twoSum(nums4, target4)}")  # Expected: [1, 3]

# Test case 5
nums5 = [0, 4, 3, 0]
target5 = 0
print(f"Test case 5: {solution.twoSum(nums5, target5)}")  # Expected: [0, 3]
