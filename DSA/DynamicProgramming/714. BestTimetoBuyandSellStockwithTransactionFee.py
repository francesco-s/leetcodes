class Solution:
    def maxProfit(self, prices, fee): 
        """
        Dynamic Programming solution.
        Time Complexity: O(n), where n is the number of days (len(prices)).
        Space Complexity: O(n), due to the free and hold arrays.
        """
        n = len(prices)
        # free[i]: max profit at day i if we do NOT hold a stock
        # hold[i]: max profit at day i if we DO hold a stock
        free, hold = [0] * n, [0] * n

        # On day 0, if we buy, profit is -prices[0]
        hold[0] = -prices[0]

        for i in range(1, n):
            # Either keep holding, or buy today (from free state)
            hold[i] = max(hold[i - 1], free[i - 1] - prices[i])
            # Either keep being free, or sell today (from hold state, pay fee)
            free[i] = max(free[i - 1], hold[i - 1] + prices[i] - fee)

        # The answer is the max profit when not holding any stock at the end
        return free[-1]

# Test cases
solution = Solution()

# Test case 1
prices1 = [1, 3, 2, 8, 4, 9]
fee1 = 2
result1 = solution.maxProfit(prices1, fee1)
print(f"Test case 1: {result1}")  # Expected: 8

# Test case 2
prices2 = [1, 3, 7, 5, 10, 3]
fee2 = 3
result2 = solution.maxProfit(prices2, fee2)
print(f"Test case 2: {result2}")  # Expected: 6

# Test case 3
prices3 = [1, 2, 3, 4, 5]
fee3 = 1
result3 = solution.maxProfit(prices3, fee3)
print(f"Test case 3: {result3}")  # Expected: 3