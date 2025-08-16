class Solution:
    def isValidSudoku2(self, board):
        n, m, s = len(board[0]), len(board), 9

        rows = [set() for _ in range(n)]
        cols = [set() for _ in range(m)]
        squares = [set() for _ in range(s)]

        for i in range(n):
            for j in range(m):
                val = board[i][j]

                if val == ".":
                    continue

                square_idx = (i // 3) * 3 + j // 3

                if val in rows[i] or val in cols[j] or val in squares[square_idx]:
                    return False

                squares[square_idx].add(val)
                rows[i].add(val)
                cols[j].add(val)

        return True
    
    def isValidSudoku(self, board):
        seen = set()
        for i in range(9):
            for j in range(9):
                val = board[i][j]
                if val == '.':
                    continue
                r = ('r', i, val)
                c = ('c', j, val)
                b = ('b', i // 3, j // 3, val)
                if r in seen or c in seen or b in seen:
                    return False
                seen.add(r); seen.add(c); seen.add(b)
        return True




# Test cases
solution = Solution()

# Test case 1: Valid board
board1 = [
    ["5","3",".",".","7",".",".",".","."],
    ["6",".",".","1","9","5",".",".","."],
    [".","9","8",".",".",".",".","6","."],
    ["8",".",".",".","6",".",".",".","3"],
    ["4",".",".","8",".","3",".",".","1"],
    ["7",".",".",".","2",".",".",".","6"],
    [".","6",".",".",".",".","2","8","."],
    [".",".",".","4","1","9",".",".","5"],
    [".",".",".",".","8",".",".","7","9"]
]
result1 = solution.isValidSudoku(board1)
print(f"Test case 1: {result1}")  # Expected: True

# Test case 2: Invalid board (duplicate '5' in first row)
board2 = [
    ["5","3",".",".","7",".",".",".","5"],
    ["6",".",".","1","9","5",".",".","."],
    [".","9","8",".",".",".",".","6","."],
    ["8",".",".",".","6",".",".",".","3"],
    ["4",".",".","8",".","3",".",".","1"],
    ["7",".",".",".","2",".",".",".","6"],
    [".","6",".",".",".",".","2","8","."],
    [".",".",".","4","1","9",".",".","5"],
    [".",".",".",".","8",".",".","7","9"]
]
result2 = solution.isValidSudoku(board2)
print(f"Test case 2: {result2}")  # Expected: False

# Test case 3: Empty board (should be valid)
board3 = [
    [".",".",".",".",".",".",".",".","."],
    [".",".",".",".",".",".",".",".","."],
    [".",".",".",".",".",".",".",".","."],
    [".",".",".",".",".",".",".",".","."],
    [".",".",".",".",".",".",".",".","."],
    [".",".",".",".",".",".",".",".","."],
    [".",".",".",".",".",".",".",".","."],
    [".",".",".",".",".",".",".",".","."],
    [".",".",".",".",".",".",".",".","."]
]
result3 = solution.isValidSudoku(board3)
print(f"Test case 3: {result3}")  # Expected: True
