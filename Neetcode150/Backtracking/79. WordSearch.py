from typing import List


class Solution:

    def exist(self, board: List[List[str]], word: str) -> bool:
        """
        Determines if the word exists in the board using DFS backtracking.
        
        Time Complexity: O(M*N*3^L)
            - In the worst-case, we start from each cell (M*N) and use DFS to check for the word.
            - For each DFS call, we explore at most 3 new directions (excluding the cell we came from) 
              for each character in the word of length L.
        
        Space Complexity: O(L)
            - The recursion stack may grow up to the length L of the word in the worst-case.
        """
        ROWS, COLS = len(board), len(board[0])

        def dfs(x, y, i):
            if i == len(word):
                return True
            if x >= ROWS or x < 0 or y >= COLS or y < 0 or board[x][y] != word[i] or board[x][y] == '#':
                return False

            temp = board[x][y]
            board[x][y] = "#"
            res = dfs(x - 1, y, i + 1) or dfs(x + 1, y, i + 1) or dfs(x, y - 1, i + 1) or dfs(x, y + 1, i + 1)
            board[x][y] = temp

            return res

        for i in range(ROWS):
            for j in range(COLS):
                if dfs(i, j, 0):
                    return True

        return False

# Test cases
solution = Solution()

# Test case 1 (example)
board1 = [["A","B","C","E"],
          ["S","F","C","S"],
          ["A","D","E","E"]]
word1 = "ABCCED"
res1 = solution.exist(board1, word1)
print(f"Test case 1: {res1}")  # Expected: True

# Test case 2 (example)
board2 = [["A","B","C","E"],
          ["S","F","C","S"],
          ["A","D","E","E"]]
word2 = "SEE"
res2 = solution.exist(board2, word2)
print(f"Test case 2: {res2}")  # Expected: True

# Test case 3 (example)
board3 = [["A","B","C","E"],
          ["S","F","C","S"],
          ["A","D","E","E"]]
word3 = "ABCB"
res3 = solution.exist(board3, word3)
print(f"Test case 3: {res3}")  # Expected: False

# Test case 4 (single row)
board4 = [["a","a","b"]]
word4 = "ab"
res4 = solution.exist(board4, word4)
print(f"Test case 4: {res4}")  # Expected: True

# Test case 5 (single column)
board5 = [["a"],["b"],["c"],["d"]]
word5 = "abcd"
res5 = solution.exist(board5, word5)
print(f"Test case 5: {res5}")  # Expected: True

# Test case 6 (revisiting not allowed)
board6 = [["a","a"]]
word6 = "aaa"
res6 = solution.exist(board6, word6)
print(f"Test case 6: {res6}")  # Expected: False
