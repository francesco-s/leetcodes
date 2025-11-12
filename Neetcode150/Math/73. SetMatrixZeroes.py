class Solution:
    def setZeroes(self, matrix):
        # Time Complexity: O(rows * cols)
        # Space Complexity: O(rows + cols)
        rows, cols = len(matrix), len(matrix[0])
        row_zero_index, col_zero_index = [False] * rows, [False] * cols

        for i in range(rows):
            for j in range(cols):
                if matrix[i][j] == 0:
                    row_zero_index[i] = True
                    col_zero_index[j] = True

        for i in range(rows):
            for j in range(cols):
                if row_zero_index[i] or col_zero_index[j]:
                    matrix[i][j] = 0

    def setZeroes(self, matrix) -> None:
        # Time Complexity: O(rows * cols)
        # Space Complexity: O(1) (in-place, excluding input)
        rows, cols = len(matrix), len(matrix[0])

        first_row_as_zeros = any(matrix[0][i] == 0 for i in range(cols))
        first_col_as_zeros = any(matrix[i][0] == 0 for i in range(rows))

        for i in range(1, rows):
            for j in range(1, cols):
                if matrix[i][j] == 0:
                    matrix[i][0] = 0
                    matrix[0][j] = 0

        for i in range(1, rows):
            for j in range(1, cols):
                if matrix[i][0] == 0 or matrix[0][j] == 0:
                    matrix[i][j] = 0

        if first_row_as_zeros:
            for i in range(cols):
                matrix[0][i] = 0

        if first_col_as_zeros:
            for i in range(rows):
                matrix[i][0] = 0


# Test cases
solution = Solution()

# Test case 1 (example)
matrix1 = [[1, 1, 1], [1, 0, 1], [1, 1, 1]]
solution.setZeroes(matrix1)
print(f"Test case 1: {matrix1}")  # Expected: [[1,0,1],[0,0,0],[1,0,1]]

# Test case 2 (example)
matrix2 = [[0, 1, 2, 0], [3, 4, 5, 2], [1, 3, 1, 5]]
solution.setZeroes(matrix2)
print(f"Test case 2: {matrix2}")  # Expected: [[0,0,0,0],[0,4,5,0],[0,3,1,0]]

# Test case 3 (single element - zero)
matrix3 = [[0]]
solution.setZeroes(matrix3)
print(f"Test case 3: {matrix3}")  # Expected: [[0]]

# Test case 4 (single element - non-zero)
matrix4 = [[1]]
solution.setZeroes(matrix4)
print(f"Test case 4: {matrix4}")  # Expected: [[1]]

# Test case 5 (single row with zero)
matrix5 = [[1, 0, 3]]
solution.setZeroes(matrix5)
print(f"Test case 5: {matrix5}")  # Expected: [[0,0,0]]

# Test case 6 (single column with zero)
matrix6 = [[1], [0], [3]]
solution.setZeroes(matrix6)
print(f"Test case 6: {matrix6}")  # Expected: [[0],[0],[0]]

# Test case 7 (no zeros)
matrix7 = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
solution.setZeroes(matrix7)
print(f"Test case 7: {matrix7}")  # Expected: [[1,2,3],[4,5,6],[7,8,9]]

# Test case 8 (multiple zeros)
matrix8 = [[0, 1, 2, 0], [3, 4, 5, 2], [1, 3, 1, 5]]
solution.setZeroes(matrix8)
print(f"Test case 8: {matrix8}")  # Expected: [[0,0,0,0],[0,4,5,0],[0,3,1,0]]
