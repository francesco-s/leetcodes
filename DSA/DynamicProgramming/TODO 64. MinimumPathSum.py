# LeetCode 64. Minimum Path Sum

class Solution:
    def minPathSum(self, grid):
        pass  # TODO: Implement solution


# Test cases
solution = Solution()

# Test case 1
grid1 = [
    [1,3,1],
    [1,5,1],
    [4,2,1]
]
result1 = solution.minPathSum(grid1)
print(f"Test case 1: {result1}")  # Expected: 7

# Test case 2
grid2 = [
    [1,2,3]
]
result2 = solution.minPathSum(grid2)
print(f"Test case 2: {result2}")  # Expected: 6

# Test case 3
grid3 = [
    [1],
    [2],
    [3]
]
result3 = solution.minPathSum(grid3)
print(f"Test case 3: {result3}")  # Expected: 6