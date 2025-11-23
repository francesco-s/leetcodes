class Solution:
    # Time Complexity: O(n), where n is the number of houses (length of nums)
    # Space Complexity: O(n), for the memoization array and recursion stack
    def rob(self, nums: list[int]) -> int:
        memo = [-1] * len(nums)

        def dp(i):
            if i >= len(nums):
                return 0
            if memo[i] != -1:
                return memo[i]
            
            memo[i] = max(dp(i + 1), nums[i] + dp(i + 2))
            return memo[i]

        return dp(0)

# Test cases
solution = Solution()

# Test case 1 (example)
nums1 = [1,2,3,1]
res1 = solution.rob(nums1)
print(f"Test case 1: {res1}")  # Expected: 4

# Test case 2 (example)
nums2 = [2,7,9,3,1]
res2 = solution.rob(nums2)
print(f"Test case 2: {res2}")  # Expected: 12

# Test case 3 (single house)
nums3 = [5]
res3 = solution.rob(nums3)
print(f"Test case 3: {res3}")  # Expected: 5

# Test case 4 (two houses)
nums4 = [2,1]
res4 = solution.rob(nums4)
print(f"Test case 4: {res4}")  # Expected: 2

# Test case 5 (all equal)
nums5 = [1,1,1,1]
res5 = solution.rob(nums5)
print(f"Test case 5: {res5}")  # Expected: 2

# Test case 6 (increasing values)
nums6 = [1,2,3,4,5]
res6 = solution.rob(nums6)
print(f"Test case 6: {res6}")  # Expected: 9  # rob 2,4,5 or 1,3,5? actually optimal is 2+4+5? (adjust after implementing)

# Test case 7 (zeros and positives)
nums7 = [0,0,5,0,10,0]
res7 = solution.rob(nums7)
print(f"Test case 7: {res7}")  # Expected: 15

# Test case 8 (large values)
nums8 = [2,105,1,7,201,8,2]
res8 = solution.rob(nums8)
print(f"Test case 8: {res8}")  # Expected: 308  # 105 + 201 + 2
