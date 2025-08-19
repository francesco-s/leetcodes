from collections import defaultdict


class Solution:
    
    def threeSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        n = len(nums)
        left, right = 0, n - 1
        res = []

        nums.sort()

        for i in range(n):
            if i > 0 and nums[i] == nums[i - 1]:
                continue
            left = i + 1
            right = n - 1
            while left < right:
                total = nums[i] + nums[left] + nums[right]
                if total == 0:
                    res.append([nums[i], nums[left], nums[right]])
                    while left < right and nums[left] == nums[left + 1]:
                        left += 1
                    while left < right and nums[right] == nums[right - 1]:
                        right -= 1
                    left += 1
                    right -= 1
                elif total < 0:
                    left += 1
                else:
                    right -= 1

        return res




# Test cases
solution = Solution()

# Test case 1
nums1 = [-1, 0, 1, 2, -1, -4]
result1 = solution.threeSum(nums1)
print(f"Test case 1: {result1}")  # Expected: [[-1, -1, 2], [-1, 0, 1]]

# Test case 2
nums2 = [0, 1, 1]
result2 = solution.threeSum(nums2)
print(f"Test case 2: {result2}")  # Expected: []

# Test case 3
nums3 = [0, 0, 0]
result3 = solution.threeSum(nums3)
print(f"Test case 3: {result3}")  # Expected: [[0, 0, 0]]

# Test case 4
nums4 = [-2, 0, 1, 1, 2]
result4 = solution.threeSum(nums4)
print(f"Test case 4: {result4}")  # Expected: [[-2, 0, 2], [-2, 1, 1]]

# Test case 5
nums5 = [-1, 0, 1, 0]
result5 = solution.threeSum(nums5)
print(f"Test case 5: {result5}")  # Expected: [[-1, 0, 1]]

# Test case 6
nums6 = [1, 2, -2, -1]
result6 = solution.threeSum(nums6)
print(f"Test case 6: {result6}")  # Expected: []
