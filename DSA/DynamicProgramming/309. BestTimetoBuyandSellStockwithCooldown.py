class Solution:
    def maxProfit(self, prices):
        if not prices:
            return 0
        n = len(prices)
        hold = [0] * n
        free = [0] * n

        hold[0] = -prices[0]

        for i in range(1, n):
            hold[i] = max(hold[i-1], (free[i-2] if i >= 2 else 0) - prices[i])
            free[i] = max(free[i-1], hold[i-1] + prices[i])

        return free[-1]


# Test cases
solution = Solution()

# Test case 1
prices1 = [1,2,3,0,2]
result1 = solution.maxProfit(prices1)
print(f"Test case 1: {result1}")  # Expected: 3

# Test case 2
prices2 = [1]
result2 = solution.maxProfit(prices2)
print(f"Test case 2: {result2}")  # Expected: 0

# Test case 3
prices3 = [2,1,4]
result3 = solution.maxProfit(prices3)
print(f"Test case 3: {result3}")  # Expected: 3