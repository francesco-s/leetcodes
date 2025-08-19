class Solution:

    def maxProfitTLE(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        global_min = 0

        for i in range(0, len(prices)):
            global_min = min(global_min, prices[i] - max(prices[i:]))
        
        return -global_min
    
    
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        global_max = 0
        min_sofar = float('inf')

        for i in range(0, len(prices)):
            if prices[i] < min_sofar:
                min_sofar = prices[i]
                
            global_max = max(global_max, prices[i] - min_sofar)
        
        return global_max



# Test cases
solution = Solution()

# Test case 1
prices1 = [7,1,5,3,6,4]
result1 = solution.maxProfit(prices1)
print(f"Test case 1: {result1}")  # Expected: 5

# Test case 2
prices2 = [7,6,4,3,1]
result2 = solution.maxProfit(prices2)
print(f"Test case 2: {result2}")  # Expected: 0

# Test case 3
prices3 = [1,2,3,4,5]
result3 = solution.maxProfit(prices3)
print(f"Test case 3: {result3}")  # Expected: 4

# Test case 4
prices4 = [2,4,1]
result4 = solution.maxProfit(prices4)
print(f"Test case 4: {result4}")  # Expected: 2

# Test case 5
prices5 = [3,3,5,0,0,3,1,4]
result5 = solution.maxProfit(prices5)
print(f"Test case 5: {result5}")  # Expected: 4

# Test case 6
prices6 = [1,2]
result6 = solution.maxProfit(prices6)
print(f"Test case 6: {result6}")  # Expected: 1
