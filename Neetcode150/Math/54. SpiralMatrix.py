from typing import List


class Solution:

    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        """
        Return elements of matrix in spiral order.

        Time Complexity: O(m * n) where m = number of rows and n = number of columns.
        Space Complexity: O(1) extra space (not counting the output list). Output list uses O(m * n).
        """
        left, right = 0, len(matrix[0])
        top, bottom = 0, len(matrix)
        res = []

        while left < right and top < bottom:
            for i in range(left, right):
                res.append(matrix[top][i])
            top += 1

            for i in range(top, bottom):
                res.append(matrix[i][right - 1])
            right -= 1

            if not (left < right and top < bottom):  # Handle non-square matrices
                break

            for i in range(right - 1, left - 1, -1):
                res.append(matrix[bottom - 1][i])
            bottom -= 1

            for i in range(bottom - 1, top - 1, -1):
                res.append(matrix[i][left])
            left += 1

        return res

# Test cases
solution = Solution()

# Test case 1 (example - 3x3)
matrix1 = [[1,2,3],[4,5,6],[7,8,9]]
res1 = solution.spiralOrder(matrix1)
print(f"Test case 1: {res1}")  # Expected: [1,2,3,6,9,8,7,4,5]

# Test case 2 (example - 3x4)
matrix2 = [[1,2,3,4],[5,6,7,8],[9,10,11,12]]
res2 = solution.spiralOrder(matrix2)
print(f"Test case 2: {res2}")  # Expected: [1,2,3,4,8,12,11,10,9,5,6,7]

# Test case 3 (single row)
matrix3 = [[1,2,3,4]]
res3 = solution.spiralOrder(matrix3)
print(f"Test case 3: {res3}")  # Expected: [1,2,3,4]

# Test case 4 (single column)
matrix4 = [[1],[2],[3],[4]]
res4 = solution.spiralOrder(matrix4)
print(f"Test case 4: {res4}")  # Expected: [1,2,3,4]

# Test case 5 (single element)
matrix5 = [[1]]
res5 = solution.spiralOrder(matrix5)
print(f"Test case 5: {res5}")  # Expected: [1]

# Test case 6 (2x2)
matrix6 = [[1,2],[3,4]]
res6 = solution.spiralOrder(matrix6)
print(f"Test case 6: {res6}")  # Expected: [1,2,4,3]

# Test case 7 (5x5)
matrix7 = [
    [1,2,3,4,5],
    [6,7,8,9,10],
    [11,12,13,14,15],
    [16,17,18,19,20],
    [21,22,23,24,25]
]
res7 = solution.spiralOrder(matrix7)
print(f"Test case 7: {res7}")  # Expected: [1,2,3,4,5,10,15,20,25,24,23,22,21,16,11,6,7,8,9,14,19,18,17,12,13]
