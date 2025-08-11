from typing import List


class Solution:
    def minFallingPathSum(self, matrix: List[List[int]]) -> int:
        min_falling_sum = float('inf')

        nrows = len(matrix)
        ncols = len(matrix[0])

        memo = {}

        def helper(row, col):
            
            if col < 0 or col >= ncols:
                return float('inf') 

            if row == nrows - 1:
                return matrix[row][col]

            if (row, col) in memo:
                return memo[(row, col)]

            bottom_left = helper(row + 1, col - 1)
            bottom = helper(row + 1, col)
            bottom_right = helper(row + 1, col + 1)

            memo[(row, col)] = min(bottom_left, bottom, bottom_right) + matrix[row][col]

            return memo[(row, col)]



        for col in range(ncols):
            min_falling_sum = min(min_falling_sum, helper(0, col))
        
        return min_falling_sum
        

# Test cases
solution = Solution()

# Test case 1
matrix1 = [
    [2,1,3],
    [6,5,4],
    [7,8,9]
]
result1 = solution.minFallingPathSum(matrix1)
print(f"Test case 1: {result1}")  # Expected: 13

# Test case 2
matrix2 = [
    [-19,57],
    [-40,-5]
]
result2 = solution.minFallingPathSum(matrix2)
print(f"Test case 2: {result2}")  # Expected: -59

# Test case 3
matrix3 = [
    [100]
]
result3 = solution.minFallingPathSum(matrix3)
print(f"Test case 3: {result3}")  # Expected: 100