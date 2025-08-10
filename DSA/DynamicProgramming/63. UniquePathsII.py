class Solution:
    def uniquePathsWithObstaclesTD(self, obstacleGrid):
        # Time Complexity: O(m * n), where m and n are the dimensions of the grid.
        # Space Complexity: O(m * n) for memoization.
        memo = {}

        m = len(obstacleGrid)
        n = len(obstacleGrid[0])

        def helper(m, n):
            if m < 0 or n < 0 or obstacleGrid[m][n] == 1:
                return 0

            if m == 0 and n == 0:
                return 1

            if (m, n) in memo:
                return memo[(m, n)]

            memo[(m, n)] = helper(m - 1, n) + helper(m, n - 1)
            return memo[(m, n)]

        return helper(m - 1, n - 1)
    


    def uniquePathsWithObstacles(self, obstacleGrid):
        # Time Complexity: O(m * n), where m and n are the dimensions of the grid.
        # Space Complexity: O(m * n) for memoization.

        if not obstacleGrid or obstacleGrid[0][0] == 1:
            return 0
        
        m = len(obstacleGrid)
        n = len(obstacleGrid[0])
        
        dp = [[0] * n for _ in range(m)]
        
        dp[0][0] = 1


        for j in range(1, n):
            if obstacleGrid[0][j] == 0:
                dp[0][j] = dp[0][j-1]
            else:
                dp[0][j] = 0
        
        for i in range(1, m):
            if obstacleGrid[i][0] == 0:
                dp[i][0] = dp[i-1][0]
            else:
                dp[i][0] = 0

        for i in range(1, m):
            for j in range(1, n):
                if obstacleGrid[i][j] == 0:
                    dp[i][j] = dp[i - 1][j] + dp[i][j - 1]
                else:
                    dp[i][j] = 0

                
        return dp[m - 1][n - 1]

        


# Test cases
solution = Solution()

# Test case 1
grid1 = [[0,0,0],[0,1,0],[0,0,0]]
result1 = solution.uniquePathsWithObstacles(grid1)
print(f"Test case 1: {result1}")  # Expected: 2

# Test case 2
grid2 = [[0,1],[0,0]]
result2 = solution.uniquePathsWithObstacles(grid2)
print(f"Test case 2: {result2}")  # Expected: 1

# Test case 3
grid3 = [[1]]
result3 = solution.uniquePathsWithObstacles(grid3)
print(f"Test case 3: {result3}")  # Expected: 0

# Test case 4
grid4 = [[0,0],[1,1],[0,0]]
result4 = solution.uniquePathsWithObstacles(grid4)
print(f"Test case 4: {result4}")  # Expected: 0