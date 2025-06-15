import math

class Solution:
    def maxProfit(self, prices):
        """
        This method should calculate the maximum profit from buying and selling stock.
        :type prices: List[int]
        :rtype: int
        """
        largest_diff = 0
        min_sofar = math.inf


        for i in range(0, len(prices)):
            if prices[i] < min_sofar:
                min_sofar = prices[i]
            else:
                largest_diff = max(largest_diff, prices[i] - min_sofar)

        return largest_diff


    def maxProfitBrute(self, prices):
        """
        This method should calculate the maximum profit from buying and selling stock.
        :type prices: List[int]
        :rtype: int
        """
        max_profit = 0

        for i in range(0, len(prices)):
            for j in range(i + 1, len(prices)):
                if prices[j] - prices[i] > max_profit:
                    max_profit = prices[j] - prices[i]

        return max_profit
                




# Test cases
solution = Solution()

# Test case 1
prices1 = [7, 1, 5, 3, 6, 4]
result1 = solution.maxProfit(prices1)
print(f"Test case 1: {result1}")  # Expected: 5

# Test case 2
prices2 = [7, 6, 4, 3, 1]
result2 = solution.maxProfit(prices2)
print(f"Test case 2: {result2}")  # Expected: 0

# Test case 3
prices3 = [1, 2, 3, 4, 5]
result3 = solution.maxProfit(prices3)
print(f"Test case 3: {result3}")  # Expected: 4