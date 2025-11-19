from typing import List


class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        # Time Complexity: O(m * n) where m is the number of rows and n is the number of columns,
        # because each cell is visited at most once.
        # Space Complexity: O(m * n) in the worst case when the grid is filled with land,
        # due to the recursion stack.
        num_rows, num_cols = len(grid), len(grid[0])
        max_area = 0

        def dfs(x, y):
            if x >= 0 and y >= 0 and x < num_rows and y < num_cols and grid[x][y] == 1:
                grid[x][y] = 0
                return 1 + dfs(x - 1, y) + dfs(x, y - 1) + dfs(x + 1, y) + dfs(x, y + 1)
            return 0

        for col in range(num_cols):
            for row in range(num_rows):
                if grid[row][col] == 1:
                    max_area = max(dfs(row, col), max_area)

        return max_area


# Test cases
solution = Solution()

# Test case 1 (example)
grid1 = [
    [0, 0, 1, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 0, 0, 0],
    [0, 1, 1, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 1, 0, 0, 1, 1, 0, 0, 1, 0, 1, 0, 0],
    [0, 1, 0, 0, 1, 1, 0, 0, 1, 1, 1, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 1, 1, 0, 0, 0, 0],
]
res1 = solution.maxAreaOfIsland(grid1)
print(f"Test case 1: {res1}")  # Expected: 6

# Test case 2 (example)
grid2 = [[0, 0, 0, 0, 0, 0, 0, 0]]
res2 = solution.maxAreaOfIsland(grid2)
print(f"Test case 2: {res2}")  # Expected: 0

# Test case 3 (single land cell)
grid3 = [[1]]
res3 = solution.maxAreaOfIsland(grid3)
print(f"Test case 3: {res3}")  # Expected: 1

# Test case 4 (all water)
grid4 = [[0, 0], [0, 0]]
res4 = solution.maxAreaOfIsland(grid4)
print(f"Test case 4: {res4}")  # Expected: 0

# Test case 5 (multiple small islands)
grid5 = [[1, 0, 1, 0], [0, 1, 0, 1], [1, 0, 1, 0]]
res5 = solution.maxAreaOfIsland(grid5)
print(f"Test case 5: {res5}")  # Expected: 1

# Test case 6 (one large island)
grid6 = [[1, 1, 1], [1, 1, 0], [0, 1, 1]]
res6 = solution.maxAreaOfIsland(grid6)
print(f"Test case 6: {res6}")  # Expected: 7
