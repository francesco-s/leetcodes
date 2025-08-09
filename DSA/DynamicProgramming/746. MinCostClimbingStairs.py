# Exercise: Min Cost Climbing Stairs (746) – Easy
# Link: https://leetcode.com/problems/min-cost-climbing-stairs/
from typing import List

class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int: # Bottom Up O(n) O(n)

        n = len(cost)
        dp = [0 for i in range(n + 1)]

        for i in range(2, n + 1):
            dp[i] = min(dp[i - 1] + cost[i - 1], dp[i - 2] + cost[i - 2])

        return dp[n]
    
    def minCostClimbingStairsTD(self, cost: List[int]) -> int: # Top Down O(n) O(n)
        def dp(i):
            if i <= 1:
                return 0
            
            if i in memo:
                return memo[i]
            
            memo[i] = min(dp(i - 1) + cost[i - 1], dp(i - 2) + cost[i - 2])
            return memo[i]
        
        memo = {}
        return dp(len(cost))

    def minCostClimbingStairsGreedy(self, cost: List[int]) -> int: # Greedy not working solution

        i = 0
        total_cost = 0

        while i < len(cost):
            if i >= len(cost) - 1 or i >= len(cost) - 2:
                break
            if cost[i + 1] < cost[i + 2]:
                _min = cost[i + 1]
                i += 1
            else:
                _min = cost[i + 2]
                i += 2

            total_cost += _min
        
        return total_cost

# Test cases
solution = Solution()

# Test case 1
cost1 = [10, 15, 20]
result1 = solution.minCostClimbingStairs(cost1)
print(f"Test case 1: {result1}")  # Expected: 15

# Test case 2
cost2 = [1, 100, 1, 1, 1, 100, 1, 1, 100, 1]
result2 = solution.minCostClimbingStairs(cost2)
print(f"Test case 2: {result2}")  # Expected: 6

# Test case 3
cost3 = [0, 0, 0, 0]
result3 = solution.minCostClimbingStairs(cost3)
print(f"Test case 3: {result3}")  # Expected: 0

# Test case 4
cost4 = [1, 2]
result4 = solution.minCostClimbingStairs(cost4)
print(f"Test case 4: {result4}")  # Expected: 1

# Test case 5
cost5 = [5]
result5 = solution.minCostClimbingStairs(cost5)
print(f"Test case 5: {result5}")  # Expected: 0