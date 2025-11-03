from typing import List


class Solution:

    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Rotate the n x n matrix 90 degrees clockwise in-place.
        Time Complexity: O(n^2)
        Space Complexity: O(1)
        """
        n = len(matrix)

        # matrix[:] = [[matrix[row][col] for row in range(n)] for col in range(n)]
        for i in range(n):
            for j in range(i):
                matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]

        for row in matrix:
            row.reverse()


# Test cases
solution = Solution()

# Test case 1 (example - 3x3)
matrix1 = [[1,2,3],[4,5,6],[7,8,9]]
solution.rotate(matrix1)
print(f"Test case 1: {matrix1}")  # Expected: [[7,4,1],[8,5,2],[9,6,3]]

# Test case 2 (example - 4x4)
matrix2 = [[5,1,9,11],[2,4,8,10],[13,3,6,7],[15,14,12,16]]
solution.rotate(matrix2)
print(f"Test case 2: {matrix2}")  # Expected: [[15,13,2,5],[14,3,4,1],[12,6,8,9],[16,7,10,11]]

# Test case 3 (1x1 - single element)
matrix3 = [[1]]
solution.rotate(matrix3)
print(f"Test case 3: {matrix3}")  # Expected: [[1]]

# Test case 4 (2x2)
matrix4 = [[1,2],[3,4]]
solution.rotate(matrix4)
print(f"Test case 4: {matrix4}")  # Expected: [[3,1],[4,2]]

# Test case 5 (5x5)
matrix5 = [
    [1,2,3,4,5],
    [6,7,8,9,10],
    [11,12,13,14,15],
    [16,17,18,19,20],
    [21,22,23,24,25]
]
solution.rotate(matrix5)
print(f"Test case 5: {matrix5}")  # Expected: [[21,16,11,6,1],[22,17,12,7,2],[23,18,13,8,3],[24,19,14,9,4],[25,20,15,10,5]]

# Test case 6 (all same values)
matrix6 = [[1,1],[1,1]]
solution.rotate(matrix6)
print(f"Test case 6: {matrix6}")  # Expected: [[1,1],[1,1]]
