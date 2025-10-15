from typing import List


class Solution:
    def solve(self, board: List[List[str]]) -> None:

        ROWS, COLS = len(board), len(board[0])

        def capture(x, y):
            if x < 0 or y < 0 or x >= ROWS or y >= COLS or board[x][y] != 'O':
                return
            
            board[x][y] = 'T'
            capture(x - 1, y)
            capture(x + 1, y)
            capture(x, y + 1)
            capture(x, y - 1)

        for r in range(ROWS):
            if board[r][0] == 'O':
                capture(r, 0)
            if board[r][COLS - 1] == 'O':
                capture(r, COLS - 1)

        for c in range(COLS):
            if board[0][c] == 'O':
                capture(0, c)
            if board[ROWS - 1][c] == 'O':
                capture(ROWS - 1, c)

        for r in range(ROWS):
            for c in range(COLS):
                if board[r][c] == 'O':
                    board[r][c] = 'X'
                elif board[r][c] == 'T':
                    board[r][c] = 'O'

        


# Test cases
solution = Solution()

# Test case 1 (example)
board1 = [
    ["X","X","X","X"],
    ["X","O","O","X"],
    ["X","X","O","X"],
    ["X","O","X","X"]
]
solution.solve(board1)
print(f"Test case 1: {board1}")  
# Expected: [
#   ["X","X","X","X"],
#   ["X","X","X","X"],
#   ["X","X","X","X"],
#   ["X","O","X","X"]
# ]

# Test case 2 (all Os)
board2 = [
    ["O","O","O"],
    ["O","O","O"],
    ["O","O","O"]
]
solution.solve(board2)
print(f"Test case 2: {board2}")
# Expected: unchanged as all Os lie on border

# Test case 3 (all Xs)
board3 = [
    ["X","X"],
    ["X","X"]
]
solution.solve(board3)
print(f"Test case 3: {board3}")
# Expected: unchanged as no Os to flip

# Test case 4 (single row)
board4 = [["O","X","O","X"]]
solution.solve(board4)
print(f"Test case 4: {board4}")
# Expected: unchanged since all Os on edge

# Test case 5 (single column)
board5 = [
    ["O"],
    ["X"],
    ["O"]
]
solution.solve(board5)
print(f"Test case 5: {board5}")
# Expected: unchanged as all Os on edge

# Test case 6 (complex shape)
board6 = [
    ["X","O","X","O","X","O"],
    ["O","X","O","X","O","X"],
    ["X","O","X","O","X","O"],
    ["O","X","O","X","O","X"]
]
solution.solve(board6)
print(f"Test case 6: {board6}")
# Expected: Os not connected to border flipped
