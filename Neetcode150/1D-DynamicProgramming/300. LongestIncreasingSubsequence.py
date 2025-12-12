from typing import List


class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        n = len(nums)
        memo = [[-1] * (n + 1) for _ in range(n)]

        def dfs(i, j):
            if i == n:
                return 0

            if memo[i][j] != -1:
                return memo[i][j]

            skip = dfs(i + 1, j)

            take = 0
            if j == n or nums[i] > nums[j]:
                take = 1 + dfs(i + 1, i)

            memo[i][j] = max(skip, take)
            return memo[i][j]

        return dfs(0, n)


# Test cases
solution = Solution()

# Test case 1 (example)
nums1 = [10, 9, 2, 5, 3, 7, 101, 18]
res1 = solution.lengthOfLIS(nums1)
print(f"Test case 1: {res1}")  # Expected: 4

# Test case 2 (example)
nums2 = [0, 1, 0, 3, 2, 3]
res2 = solution.lengthOfLIS(nums2)
print(f"Test case 2: {res2}")  # Expected: 4

# Test case 3 (example - all same)
nums3 = [7, 7, 7, 7, 7, 7, 7]
res3 = solution.lengthOfLIS(nums3)
print(f"Test case 3: {res3}")  # Expected: 1

# Test case 4 (strictly increasing)
nums4 = [1, 2, 3, 4, 5]
res4 = solution.lengthOfLIS(nums4)
print(f"Test case 4: {res4}")  # Expected: 5

# Test case 5 (strictly decreasing)
nums5 = [5, 4, 3, 2, 1]
res5 = solution.lengthOfLIS(nums5)
print(f"Test case 5: {res5}")  # Expected: 1

# Test case 6 (single element)
nums6 = [1]
res6 = solution.lengthOfLIS(nums6)
print(f"Test case 6: {res6}")  # Expected: 1

# Test case 7 (alternating)
nums7 = [1, 3, 6, 7, 9, 4, 10, 5, 6]
res7 = solution.lengthOfLIS(nums7)
print(f"Test case 7: {res7}")  # Expected: 6
