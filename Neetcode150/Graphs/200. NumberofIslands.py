class Solution:

    def numIslands(self, grid):
        """
        :type grid: List[List[str]]  # '1' for land, '0' for water
        :rtype: int

        Time Complexity (TC): O(n * m) where n is the number of rows and m is the number of columns.
        Space Complexity (SC): O(n * m) in the worst case due to recursion stack.
        """

        num_rows, num_cols = len(grid), len(grid[0])
        num_islands = 0

        def dfs(x, y):
            if x >= 0 and y >= 0 and x < num_rows and y < num_cols and grid[x][y] == "1":
                grid[x][y] = "0"
                dfs(x - 1, y)
                dfs(x, y - 1)
                dfs(x + 1, y)
                dfs(x, y + 1)
            return

        for col in range(num_cols):
            for row in range(num_rows):
                if grid[row][col] == "1":
                    dfs(row, col)
                    num_islands += 1

        return num_islands
            

# Test cases
solution = Solution()

# Test case 1 (example)
grid1 = [
    ["1","1","1","1","0"],
    ["1","1","0","1","0"],
    ["1","1","0","0","0"],
    ["0","0","0","0","0"],
]
res1 = solution.numIslands(grid1)
print(f"Test case 1: {res1}")  # Expected: 1

# Test case 2 (example)
grid2 = [
    ["1","1","0","0","0"],
    ["1","1","0","0","0"],
    ["0","0","1","0","0"],
    ["0","0","0","1","1"],
]
res2 = solution.numIslands(grid2)
print(f"Test case 2: {res2}")  # Expected: 3

# Test case 3 (single land)
grid3 = [["1"]]
res3 = solution.numIslands(grid3)
print(f"Test case 3: {res3}")  # Expected: 1

# Test case 4 (all water)
grid4 = [["0","0"],["0","0"]]
res4 = solution.numIslands(grid4)
print(f"Test case 4: {res4}")  # Expected: 0

# Test case 5 (one row)
grid5 = [["1","0","1","1","0","1"]]
res5 = solution.numIslands(grid5)
print(f"Test case 5: {res5}")  # Expected: 3

# Test case 6 (one column)
grid6 = [["1"],["0"],["1"],["1"],["0"],["1"]]
res6 = solution.numIslands(grid6)
print(f"Test case 6: {res6}")  # Expected: 3
