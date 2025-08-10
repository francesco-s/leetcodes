class Solution:
    def maxProfit(self, k, prices):
        # TODO: Implement solution
        pass

# Test cases
solution = Solution()

# Test case 1
k1 = 2
prices1 = [2, 4, 1]
result1 = solution.maxProfit(k1, prices1)
print(f"Test case 1: {result1}")  # Expected: 2

# Test case 2
k2 = 2
prices2 = [3, 2, 6, 5, 0, 3]
result2 = solution.maxProfit(k2, prices2)
print(f"Test case 2: {result2}")  # Expected: 7

# Test case 3
k3 = 1
prices3 = [1, 2]
result3 = solution.maxProfit(k3, prices3)
print(f"Test case 3: {result3}")  # Expected: 1

# Test case 4
k4 = 0
prices4 = [1, 2, 3, 4, 5]
result4 = solution.maxProfit(k4, prices4)
print(f"Test case 4: {result4}")  # Expected: 0

# Test case 5
k5 = 3
prices5 = []
result5 = solution.maxProfit(k5, prices5)
print(f"Test case 5: {result5}")  # Expected: 0