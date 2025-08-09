# Exercise: Climbing Stairs (70) – Easy
# Link: https://leetcode.com/problems/climbing-stairs/

class Solution:
    def climbStairsBrute(self, n): #O(2^n) O(n)

        def helper(curr, n):
            if curr > n:
                return 0
            if curr == n:
                return 1

            return helper(curr + 1, n) + helper(curr + 2, n)
            

        return helper(0, n)

    def climbStairsMemo(self, n): # O(n) O(n)
        memo = [0] * (n + 1)

        def helper(curr, n):
            if curr > n:
                return 0
            if curr == n:
                return 1
            if memo[curr] > 0:
                return memo[curr]

            memo[curr] = helper(curr + 1, n) + helper(curr + 2, n)
            return memo[curr]

        return helper(0, n)
    
    def climbStairs(self, n: int) -> int: # DP approach: O(n) O(n)
        if n == 1 or n == 0:
            return 1
        
        dp = [0 for i in range(n + 1)]

        dp[1] = 1
        dp[2] = 2

        for i in range(3, n + 1):
            dp[i] = dp[i - 1] + dp[i - 2]

        return dp[-1]

# Test cases
solution = Solution()

# Test case 1
n1 = 2
result1 = solution.climbStairs(n1)
print(f"Test case 1: {result1}")  # Expected: 2

# Test case 2
n2 = 3
result2 = solution.climbStairs(n2)
print(f"Test case 2: {result2}")  # Expected: 3

# Test case 3
n3 = 1
result3 = solution.climbStairs(n3)
print(f"Test case 3: {result3}")  # Expected: 1

# Test case 4
n4 = 5
result4 = solution.climbStairs(n4)
print(f"Test case 4: {result4}")  # Expected: 8

# Test case 5
n5 = 0
result5 = solution.climbStairs(n5)
print(f"Test case 5: {result5}")  # Expected: 1
