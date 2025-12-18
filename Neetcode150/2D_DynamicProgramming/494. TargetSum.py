class Solution:
    # TC: O(n * S), where n = len(nums), S = sum(nums) * 2 (range of possible sums)
    # SC: O(n * S) for memo table + O(n) recursion stack
    def findTargetSumWays(self, nums: list[int], target: int) -> int:
        memo = {}

        def dfs(i, amount):
            if i == len(nums) and amount == target:
                return 1
            if i == len(nums) and amount != target:
                return 0

            if (i, amount) in memo:
                return memo[(i, amount)]

            memo[(i, amount)] = dfs(i + 1, amount + nums[i]) + dfs(
                i + 1, amount - nums[i]
            )

            return memo[(i, amount)]

        return dfs(0, 0)


# Test cases
solution = Solution()

# Test case 1 (example)
nums1 = [1, 1, 1, 1, 1]
target1 = 3
res1 = solution.findTargetSumWays(nums1, target1)
print(f"Test case 1: {res1}")  # Expected: 5

# Test case 2 (example)
nums2 = [1]
target2 = 1
res2 = solution.findTargetSumWays(nums2, target2)
print(f"Test case 2: {res2}")  # Expected: 1

# Test case 3 (unreachable)
nums3 = [2]
target3 = 3
res3 = solution.findTargetSumWays(nums3, target3)
print(f"Test case 3: {res3}")  # Expected: 0

# Test case 4 (target larger than sum)
nums4 = [1, 2]
target4 = 10
res4 = solution.findTargetSumWays(nums4, target4)
print(f"Test case 4: {res4}")  # Expected: 0

# Test case 5 (all zeros - important edge case)
nums5 = [0, 0, 0]
target5 = 0
res5 = solution.findTargetSumWays(nums5, target5)
print(f"Test case 5: {res5}")  # Expected: 8 (2^3 ways)

# Test case 6 (mixed values)
nums6 = [1, 2, 3]
target6 = 0
res6 = solution.findTargetSumWays(nums6, target6)
print(f"Test case 6: {res6}")  # Expected: 2 (+1+2-3, -1-2+3)

# Test case 7 (absolute sum matches target)
nums7 = [1, 1]
target7 = 2
res7 = solution.findTargetSumWays(nums7, target7)
print(f"Test case 7: {res7}")  # Expected: 1 (+1+1)
