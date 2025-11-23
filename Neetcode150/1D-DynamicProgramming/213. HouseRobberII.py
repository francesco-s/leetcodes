from typing import List


# Time Complexity: O(n), where n is the number of houses. We solve two linear subproblems, each O(n).
# Space Complexity: O(n), due to the memoization array used in each subproblem.

class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return nums[0]

        def rob_linear(nums):
            memo = [-1] * len(nums)

            def dp(i):
                if i >= len(nums):
                    return 0
                
                if memo[i] != -1:
                    return memo[i]
                
                memo[i] = max(dp(i + 1), nums[i] + dp(i + 2))
                return memo[i]

            return dp(0)

        
        return max(rob_linear(nums[:-1]), rob_linear(nums[1:]))

# Test cases
solution = Solution()

# Test case 1 (example)
nums1 = [2,3,2]
res1 = solution.rob(nums1)
print(f"Test case 1: {res1}")  # Expected: 3

# Test case 2 (example)
nums2 = [1,2,3,1]
res2 = solution.rob(nums2)
print(f"Test case 2: {res2}")  # Expected: 4

# Test case 3 (example)
nums3 = [1,2,3]
res3 = solution.rob(nums3)
print(f"Test case 3: {res3}")  # Expected: 3

# Test case 4 (single element)
nums4 = [1]
res4 = solution.rob(nums4)
print(f"Test case 4: {res4}")  # Expected: 1

# Test case 5 (empty)
nums5 = []
res5 = solution.rob(nums5)
print(f"Test case 5: {res5}")  # Expected: 0

# Test case 6 (all same values)
nums6 = [2,2,2,2,2]
res6 = solution.rob(nums6)
print(f"Test case 6: {res6}")  # Expected: 4

# Test case 7 (two elements)
nums7 = [1,2]
res7 = solution.rob(nums7)
print(f"Test case 7: {res7}")  # Expected: 2

# Test case 8 (large example)
nums8 = [2,7,9,3,1]
res8 = solution.rob(nums8)
print(f"Test case 8: {res8}")  # Expected: 11
