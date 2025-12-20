class Solution:
    # Time Complexity: O(n), where n is the length of cost. Each state is computed once.
    # Space Complexity: O(n), for the recursion stack and cache.
    def minCostClimbingStairs(self, cost: list[int]) -> int:
        cache = [-1] * (len(cost) + 1)

        def dp(i):
            if i >= len(cost):
                return 0

            if cache[i] != -1:
                return cache[i]

            cache[i] = cost[i] + min(dp(i + 1), dp(i + 2))
            return cache[i]

        return min(dp(0), dp(1))


# Test cases
solution = Solution()

# Test case 1 (example)
cost1 = [10, 15, 20]
res1 = solution.minCostClimbingStairs(cost1)
print(f"Test case 1: {res1}")  # Expected: 15

# Test case 2 (example)
cost2 = [1, 100, 1, 1, 1, 100, 1, 1, 100, 1]
res2 = solution.minCostClimbingStairs(cost2)
print(f"Test case 2: {res2}")  # Expected: 6

# Test case 3 (two stairs)
cost3 = [0, 1]
res3 = solution.minCostClimbingStairs(cost3)
print(f"Test case 3: {res3}")  # Expected: 0

# Test case 4 (minimal 3 stairs, pick min)
cost4 = [20, 15, 10]
res4 = solution.minCostClimbingStairs(cost4)
print(f"Test case 4: {res4}")  # Expected: 15

# Test case 5 (all costs zero)
cost5 = [0, 0, 0, 0]
res5 = solution.minCostClimbingStairs(cost5)
print(f"Test case 5: {res5}")  # Expected: 0

# Test case 6 (incremental costs)
cost6 = [1, 2, 3, 4, 5]
res6 = solution.minCostClimbingStairs(cost6)
print(f"Test case 6: {res6}")  # Expected: 6

# Test case 7 (skip expensive step)
cost7 = [5, 100, 5, 5]
res7 = solution.minCostClimbingStairs(cost7)
print(f"Test case 7: {res7}")  # Expected: 10

# Test case 8 (single step)
cost8 = [3]
res8 = solution.minCostClimbingStairs(cost8)
print(f"Test case 8: {res8}")  # Expected: 0
