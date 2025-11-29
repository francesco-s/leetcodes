from typing import List


class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        """
        Time Complexity: O(n) - single pass through array
        Space Complexity: O(1) - only constant extra space
        
        Approach: (KADANE) Track both max and min products ending at each position.
        Min tracking is crucial since negative * negative = positive.
        """
        best_max = nums[0]
        current_max = nums[0]
        current_min = nums[0]

        for num in nums[1:]:
            prev_max = current_max
            prev_min = current_min
            
            current_max = max(num, prev_max * num, prev_min * num)
            current_min = min(num, prev_max * num, prev_min * num)
            
            best_max = max(best_max, current_max)
            
        return best_max

    def maxProduct_dp(self, nums: List[int]) -> int:
        """
        Time Complexity: O(n) - single pass through array
        Space Complexity: O(n) - uses DP arrays for max and min values
        
        Approach: Same logic as above but using arrays to store intermediate
        max/min products at each index for better readability.
        """
        n = len(nums)
        max_dp = [0] * n
        min_dp = [0] * n

        max_dp[0] = nums[0]
        min_dp[0] = nums[0]
        best = nums[0]

        for i in range(1, n):
            candidates = [nums[i], max_dp[i-1] * nums[i], min_dp[i-1] * nums[i]]
            max_dp[i] = max(candidates)
            min_dp[i] = min(candidates)
            best = max(best, max_dp[i])

        return best

# Test cases
solution = Solution()

# Test case 1 (example)
nums1 = [2,3,-2,4]
res1 = solution.maxProduct(nums1)
print(f"Test case 1: {res1}")  # Expected: 6

# Test case 2 (example)
nums2 = [-2,0,-1]
res2 = solution.maxProduct(nums2)
print(f"Test case 2: {res2}")  # Expected: 0

# Test case 3 (negative sandwich)
nums3 = [-2,3,-4]
res3 = solution.maxProduct(nums3)
print(f"Test case 3: {res3}")  # Expected: 24

# Test case 4 (single negative)
nums4 = [-2]
res4 = solution.maxProduct(nums4)
print(f"Test case 4: {res4}")  # Expected: -2

# Test case 5 (zeros involved)
nums5 = [0, 2]
res5 = solution.maxProduct(nums5)
print(f"Test case 5: {res5}")  # Expected: 2

# Test case 6 (all negatives)
nums6 = [-2, -3, -4]
res6 = solution.maxProduct(nums6)
print(f"Test case 6: {res6}")  # Expected: 12

# Test case 7 (complex alternating)
nums7 = [-2, 1, -3, 4, -1, 2, 1, -5, 4]
res7 = solution.maxProduct(nums7)
print(f"Test case 7: {res7}")  # Expected: 960
