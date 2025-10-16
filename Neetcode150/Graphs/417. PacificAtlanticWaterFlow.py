from typing import List


class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        """
        Time Complexity: O(R * C) where R is number of rows and C is number of columns.
        Each cell is visited at most twice (once from Pacific, once from Atlantic).
        Space Complexity: O(R * C) for the visited sets and worst-case recursion stack.
        """

        if not heights or not heights[0]:
            return []

        ROWS, COLS = len(heights), len(heights[0])
        atl, pac = set(), set()

        def dfs(x, y, visited, prev_height):
            if (x, y) in visited or x < 0 or y < 0 or x >= ROWS or y >= COLS or heights[x][y] < prev_height:
                return

            visited.add((x, y))
            dfs(x + 1, y, visited, heights[x][y])
            dfs(x - 1, y, visited, heights[x][y])
            dfs(x, y + 1, visited, heights[x][y])
            dfs(x, y - 1, visited, heights[x][y])


        for row in range(ROWS):
            dfs(row, 0, pac, heights[row][0])
            dfs(row, COLS - 1, atl, heights[row][COLS - 1])

        for col in range(COLS):
            dfs(0, col, pac, heights[0][col])
            dfs(ROWS - 1, col, atl, heights[ROWS - 1][col])

        res = []
        for r in range(ROWS):
            for c in range(COLS):
                if (r, c) in pac and (r, c) in atl:
                    res.append([r, c])

        return res

        

# Test cases
solution = Solution()

# Test case 1 (example)
heights1 = [
    [1,2,2,3,5],
    [3,2,3,4,4],
    [2,4,5,3,1],
    [6,7,1,4,5],
    [5,1,1,2,4]
]
res1 = solution.pacificAtlantic(heights1)
print(f"Test case 1: {res1}")  
# Expected: [[0,4],[1,3],[1,4],[2,2],[3,0],[3,1],[4,0]] in any order

# Test case 2 (example small)
heights2 = [[1]]
res2 = solution.pacificAtlantic(heights2)
print(f"Test case 2: {res2}")
# Expected: [[0,0]]

# Test case 3 (single row)
heights3 = [[1,2,3,4]]
res3 = solution.pacificAtlantic(heights3)
print(f"Test case 3: {res3}")
# Expected: all cells reach both

# Test case 4 (single column)
heights4 = [[1],[2],[3],[4]]
res4 = solution.pacificAtlantic(heights4)
print(f"Test case 4: {res4}")
# Expected: all cells reach both

# Test case 5 (all same height)
heights5 = [
    [1,1,1],
    [1,1,1],
    [1,1,1]
]
res5 = solution.pacificAtlantic(heights5)
print(f"Test case 5: {res5}")
# Expected: all cells [[0,0],[0,1],[0,2],[1,0],[1,1],[1,2],[2,0],[2,1],[2,2]]

# Test case 6 (2x2 grid)
heights6 = [
    [10,10],
    [10,10]
]
res6 = solution.pacificAtlantic(heights6)
print(f"Test case 6: {res6}")
# Expected: [[0,0],[0,1],[1,0],[1,1]]
