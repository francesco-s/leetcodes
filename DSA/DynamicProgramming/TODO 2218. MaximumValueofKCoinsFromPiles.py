class Solution:
    def maxValueOfCoins(self, piles, k):
        pass  # TODO: implement solution


# Test cases
solution = Solution()

# Test case 1
piles1 = [[1,100,3],[7,8,9]]
k1 = 2
result1 = solution.maxValueOfCoins(piles1, k1)
print(f"Test case 1: {result1}")  # Expected: 101

# Test case 2
piles2 = [[100],[100],[100],[100],[100]]
k2 = 5
result2 = solution.maxValueOfCoins(piles2, k2)
print(f"Test case 2: {result2}")  # Expected: 500

# Test case 3
piles3 = [[1,2,3,4,5,6,7],[1,2,3,4,5],[1,2,3,4],[1,2,3],[1,2],[1]]
k3 = 10
result3 = solution.maxValueOfCoins(piles3, k3)
print(f"Test case 3: {result3}")  # Expected: 28