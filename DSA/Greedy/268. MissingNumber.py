from typing import List


class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        # Time Complexity: O(n)
        # Space Complexity: O(1)
        res = len(nums)

        for i in range(
            res
        ):  # from 0 to len(nums) - 1 (we need the n -> start res to n)
            res ^= i ^ nums[i]

        return res

    def missingNumber(self, nums):
        # Time Complexity: O(n)
        # Space Complexity: O(1)
        return sum(range(len(nums) + 1)) - sum(nums)


# Test cases
solution = Solution()

# Test case 1 (example)
nums1 = [3, 0, 1]
res1 = solution.missingNumber(nums1)
print(f"Test case 1: {res1}")  # Expected: 2

# Test case 2 (example)
nums2 = [0, 1]
res2 = solution.missingNumber(nums2)
print(f"Test case 2: {res2}")  # Expected: 2

# Test case 3 (example - larger array)
nums3 = [9, 6, 4, 2, 3, 5, 7, 0, 1]
res3 = solution.missingNumber(nums3)
print(f"Test case 3: {res3}")  # Expected: 8

# Test case 4 (missing first number)
nums4 = [1, 2, 3, 4, 5]
res4 = solution.missingNumber(nums4)
print(f"Test case 4: {res4}")  # Expected: 0

# Test case 5 (missing last number)
nums5 = [0, 1, 2, 3, 4, 5, 6, 7, 8]
res5 = solution.missingNumber(nums5)
print(f"Test case 5: {res5}")  # Expected: 9

# Test case 6 (single element - zero)
nums6 = [0]
res6 = solution.missingNumber(nums6)
print(f"Test case 6: {res6}")  # Expected: 1

# Test case 7 (single element - one)
nums7 = [1]
res7 = solution.missingNumber(nums7)
print(f"Test case 7: {res7}")  # Expected: 0

# Test case 8 (missing middle)
nums8 = [0, 1, 3]
res8 = solution.missingNumber(nums8)
print(f"Test case 8: {res8}")  # Expected: 2
