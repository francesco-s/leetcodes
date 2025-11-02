class Solution:
    def maxSubArray(self, nums):
        """
        Kadane's algorithm.
        Time Complexity: O(n) where n = len(nums)
        Space Complexity: O(1) extra space
        """
        best_max = nums[0]
        current_max = nums[0]

        for num in nums[1:]:
            current_max = max(num, current_max + num)
            best_max = max(best_max, current_max)

        return best_max

    def max_subarray_dp(nums):
        n = len(nums)
        dp = [0] * n

        dp[0] = nums[0]
        best = dp[0]

        for i in range(1, n):
            dp[i] = max(nums[i], dp[i - 1] + nums[i])
            best = max(best, dp[i])

        return best


# Test cases
solution = Solution()

# Test case 1 (example)
nums1 = [-2, 1, -3, 4, -1, 2, 1, -5, 4]
res1 = solution.maxSubArray(nums1)
print(f"Test case 1: {res1}")  # Expected: 6 (subarray [4,-1,2,1])

# Test case 2 (single element)
nums2 = [1]
res2 = solution.maxSubArray(nums2)
print(f"Test case 2: {res2}")  # Expected: 1

# Test case 3 (all positive)
nums3 = [5, 4, -1, 7, 8]
res3 = solution.maxSubArray(nums3)
print(f"Test case 3: {res3}")  # Expected: 23

# Test case 4 (all negative)
nums4 = [-3, -2, -5, -1, -4]
res4 = solution.maxSubArray(nums4)
print(f"Test case 4: {res4}")  # Expected: -1

# Test case 5 (alternating signs)
nums5 = [1, -2, 3, -4, 5]
res5 = solution.maxSubArray(nums5)
print(f"Test case 5: {res5}")  # Expected: 5

# Test case 6 (large positive at end)
nums6 = [-2, -3, -1, 100]
res6 = solution.maxSubArray(nums6)
print(f"Test case 6: {res6}")  # Expected: 100
