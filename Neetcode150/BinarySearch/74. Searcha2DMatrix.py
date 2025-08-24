from typing import List


class Solution:
    # Time Complexity: O(log(m * n)), where m is the number of rows and n is the number of columns.
    # Space Complexity: O(1), since we use only constant extra space.
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        """
        Searches for a target value in a 2D matrix using binary search.
        The matrix is assumed to have the following properties:
        - Integers in each row are sorted from left to right.
        - The first integer of each row is greater than the last integer of the previous row.
        Args:
            matrix (List[List[int]]): 2D list of integers.
            target (int): The integer value to search for.
        Returns:
            bool: True if the target is found in the matrix, False otherwise.
        Notes:
            The matrix is treated as a flattened 1D array for binary search.
            - 'middle // n' gives the row index in the matrix.
            - 'middle % n' gives the column index in the matrix.
            This mapping allows efficient access to elements as if the matrix were a single sorted list.
        """
        m = len(matrix)

        if m == 0:
            return False
        
        n = len(matrix[0])
        left = 0
        right = m * n - 1

        while left <= right:
            middle = left + ((right - left) // 2)
            pivot = matrix[middle // n][middle % n]

            if pivot == target:
                return True
            elif pivot < target:
                left = middle + 1
            else:
                right = middle - 1
        
        return False
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        # Time Complexity: O(log m + log n), where m is the number of rows and n is the number of columns.
        # Space Complexity: O(1), since we use only constant extra space.

        right_row = float('inf')

        # Use binary search to find the correct row
        top, bottom = 0, len(matrix) - 1
        while top <= bottom:
            mid = top + (bottom - top) // 2
            if matrix[mid][-1] < target:
                top = mid + 1
            else:
                right_row = mid
                bottom = mid - 1
        
        if right_row == float('inf'):
            return False

        left, right = 0, len(matrix[right_row]) - 1

        while left <= right:
            middle = left + ((right - left) // 2)
            if matrix[right_row][middle] == target:
                return True

            if matrix[right_row][middle] < target:
                left = middle + 1
            else:
                right = middle - 1

        return False

        
        

# Test cases
solution = Solution()

# Test case 1
matrix1 = [[1,3,5,7],[10,11,16,20],[23,30,34,50]]
target1 = 3
result1 = solution.searchMatrix(matrix1, target1)
print(f"Test case 1: {result1}")  # Expected: True

# Test case 2
matrix2 = [[1,3,5,7],[10,11,16,20],[23,30,34,50]]
target2 = 13
result2 = solution.searchMatrix(matrix2, target2)
print(f"Test case 2: {result2}")  # Expected: False

# Test case 3
matrix3 = [[1]]
target3 = 1
result3 = solution.searchMatrix(matrix3, target3)
print(f"Test case 3: {result3}")  # Expected: True

# Test case 4
matrix4 = [[1,4,7,11],[2,5,8,12],[3,6,9,16]]
target4 = 5
result4 = solution.searchMatrix(matrix4, target4)
print(f"Test case 4: {result4}")  # Expected: True

# Test case 5
matrix5 = [[1,4,7,11],[2,5,8,12],[3,6,9,16]]
target5 = 20
result5 = solution.searchMatrix(matrix5, target5)
print(f"Test case 5: {result5}")  # Expected: False

# Test case 6
matrix6 = [[1,3,5]]
target6 = 3
result6 = solution.searchMatrix(matrix6, target6)
print(f"Test case 6: {result6}")  # Expected: True
