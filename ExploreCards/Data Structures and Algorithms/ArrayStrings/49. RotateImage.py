class Solution:
    def rotate2(self, matrix):
        """
        Rotates the given n x n 2D matrix 90 degrees clockwise in place.
        :param matrix: List[List[int]]
        :return: None
        """
        n = len(matrix) - 1

        temp = matrix[n][0]
        matrix[n][0] = matrix[n][n]
        matrix[n][n] = matrix[0][n]
        matrix[0][n] = matrix[0][0]
        matrix[0][0] = temp

        temp = matrix[n][n - 1]
        matrix[n][n - 1] = matrix[n - 2][n]
        matrix[n - 2][n] = matrix[0][n - 2]
        matrix[0][n - 2] = matrix[n - 1][0]
        matrix[n - 1][0] = temp

        # temp = matrix[n][-2]
        # matrix[n][-2] = matrix[1][n]
        # matrix[1][n] = matrix[0][1]
        # matrix[0][1] = matrix[2][0]
        # matrix[2][0] = temp




        print('\n'.join(['\t'.join([str(cell) for cell in row]) for row in matrix]))

    def rotate(self, matrix):
        """
        Rotates the given n x n 2D matrix 90 degrees clockwise in place.
        :param matrix: List[List[int]]
        :return: None
        """
        # Transpose the matrix
        for i in range(len(matrix)):
            for j in range(i + 1, len(matrix)):
                matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]
            matrix[i].reverse() # Reverse here

        # Reverse each row
        # for row in matrix:
        #     row.reverse()

# Test cases
solution = Solution()

# Test case 1
matrix1 = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]
solution.rotate(matrix1)
print(f"Test case 1: {matrix1}")  # Expected: [[7, 4, 1], [8, 5, 2], [9, 6, 3]]

# Test case 2
matrix2 = [
    [5, 1, 9, 11],
    [2, 4, 8, 10],
    [13, 3, 6, 7],
    [15, 14, 12, 16]
]
solution.rotate(matrix2)
print(f"Test case 2: {matrix2}")  # Expected: [[15, 13, 2, 5], [14, 3, 4, 1], [12, 6, 8, 9], [16, 7, 10, 11]]

# Test case 3
matrix3 = [[1]]
solution.rotate(matrix3)
print(f"Test case 3: {matrix3}")  # Expected: [[1]]

# Test case 4
matrix4 = [
    [1, 2],
    [3, 4]
]
solution.rotate(matrix4)
print(f"Test case 4: {matrix4}")  # Expected: [[3, 1], [4, 2]]