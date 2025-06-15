class Solution:
    def maxProfit(self, prices):
        """
        This method should calculate the maximum profit from stock prices.
        :type prices: List[int]
        :rtype: int
        """
        max_profit = 0
        for i in  range(1, len(prices)):
            if prices[i] > prices[i - 1]:
                max_profit +=  prices[i] - prices[i - 1]

        return max_profit

# Test cases
solution = Solution()

# Test case 1
prices1 = [7, 1, 5, 3, 6, 4]
result1 = solution.maxProfit(prices1)
print(f"Test case 1: {result1}")  # Expected: 7

# Test case 2
prices2 = [1, 2, 3, 4, 5]
result2 = solution.maxProfit(prices2)
print(f"Test case 2: {result2}")  # Expected: 4

# Test case 3
prices3 = [7, 6, 4, 3, 1]
result3 = solution.maxProfit(prices3)
print(f"Test case 3: {result3}")  # Expected: 0