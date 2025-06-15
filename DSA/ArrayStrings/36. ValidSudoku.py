class Solution:
    def isValidSudoku(self, board):
        """
        Determines if a 9x9 Sudoku board is valid.
        :type board: List[List[str]]
        :rtype: bool
        """
        
        columns_numbers = [set() for _ in range(len(board))]
        rows_numbers = [set() for _ in range(len(board))]
        square_numbers = [set() for _ in range(len(board))]

        i, j = 0, 0

        while i < len(board):
            j = 0
            while j < len(board):
                if board[i][j] != ".":
                    if board[i][j] not in rows_numbers[i]:
                        rows_numbers[i].add(board[i][j])
                    else:
                        return False
                    if board[i][j] not in columns_numbers[j]:
                        columns_numbers[j].add(board[i][j])
                    else:
                        return False
                    
                    square_index = (i // 3) * 3 + j // 3
                    if board[i][j] not in square_numbers[square_index]:
                        square_numbers[square_index].add(board[i][j])
                    else:
                        return False
                j += 1
            i += 1
        
        return True


# Test cases
solution = Solution()

# Test case 1
board1 = [
    ["5", "3", ".", ".", "7", ".", ".", ".", "."],
    ["6", ".", ".", "1", "9", "5", ".", ".", "."],
    [".", "9", "8", ".", ".", ".", ".", "6", "."],
    ["8", ".", ".", ".", "6", ".", ".", ".", "3"],
    ["4", ".", ".", "8", ".", "3", ".", ".", "1"],
    ["7", ".", ".", ".", "2", ".", ".", ".", "6"],
    [".", "6", ".", ".", ".", ".", "2", "8", "."],
    [".", ".", ".", "4", "1", "9", ".", ".", "5"],
    [".", ".", ".", ".", "8", ".", ".", "7", "9"]
]
print(f"Test case 1: {solution.isValidSudoku(board1)}")  # Expected: True

# Test case 2
board2 = [
    ["8", "3", ".", ".", "7", ".", ".", ".", "."],
    ["6", ".", ".", "1", "9", "5", ".", ".", "."],
    [".", "9", "8", ".", ".", ".", ".", "6", "."],
    ["8", ".", ".", ".", "6", ".", ".", ".", "3"],
    ["4", ".", ".", "8", ".", "3", ".", ".", "1"],
    ["7", ".", ".", ".", "2", ".", ".", ".", "6"],
    [".", "6", ".", ".", ".", ".", "2", "8", "."],
    [".", ".", ".", "4", "1", "9", ".", ".", "5"],
    [".", ".", ".", ".", "8", ".", ".", "7", "9"]
]
print(f"Test case 2: {solution.isValidSudoku(board2)}")  # Expected: False