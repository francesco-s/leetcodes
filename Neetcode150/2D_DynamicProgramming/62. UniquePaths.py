class Solution:
    """
    Time Complexity (TC) = O(m × n)
        Each cell (i, j) in the grid is computed once and stored in memo. Subsequent calls reuse the stored value.

    Space Complexity (SC): O(m × n)
        memo table takes m × n space
        Recursive call stack can go up to (m + n) in the worst case
    """

    def uniquePaths(self, m: int, n: int) -> int:
        memo = [[-1] * m for _ in range(n)]

        def dfs(i, j):
            if i == (n - 1) and j == (m - 1):
                return 1
            if i >= n or j >= m:
                return 0
            memo[i][j] = dfs(i + 1, j) + dfs(i, j + 1)
            return memo[i][j]

        return dfs(0, 0)


# Test cases
solution = Solution()

# Test case 1 (example)
m1, n1 = 3, 7
res1 = solution.uniquePaths(m1, n1)
print(f"Test case 1: {res1}")  # Expected: 28

# Test case 2 (example)
m2, n2 = 3, 2
res2 = solution.uniquePaths(m2, n2)
print(f"Test case 2: {res2}")  # Expected: 3

# Test case 3 (single cell)
m3, n3 = 1, 1
res3 = solution.uniquePaths(m3, n3)
print(f"Test case 3: {res3}")  # Expected: 1

# Test case 4 (single row)
m4, n4 = 1, 10
res4 = solution.uniquePaths(m4, n4)
print(f"Test case 4: {res4}")  # Expected: 1

# Test case 5 (single column)
m5, n5 = 10, 1
res5 = solution.uniquePaths(m5, n5)
print(f"Test case 5: {res5}")  # Expected: 1

# Test case 6 (square grid)
m6, n6 = 3, 3
res6 = solution.uniquePaths(m6, n6)
print(f"Test case 6: {res6}")  # Expected: 6

# Test case 7 (larger grid)
m7, n7 = 7, 3
res7 = solution.uniquePaths(m7, n7)
print(f"Test case 7: {res7}")  # Expected: 28 (symmetry with case 1)
