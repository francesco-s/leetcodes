import collections
from typing import List


class Solution(object):
    def nearestExit(self, maze: List[List[str]], entrance: List[int]) -> int:

        queue = collections.deque()
        rows, cols = len(maze), len(maze[0])

        maze[entrance[0]][entrance[1]] = ':)'
        queue.append([entrance[0], entrance[1], 0])

        while queue:
            current_row, current_col, current_dist = queue.popleft()
            for mov in ((1, 0), (-1, 0), (0, 1), (0, -1)):
                next_row = current_row + mov[0]
                next_col = current_col + mov[1]

                if 0 <= next_row < rows and 0 <= next_col < cols and maze[next_row][next_col] == '.':

                    if next_row == 0 or next_row == rows - 1 or next_col == 0 or next_col == cols - 1:  # exit case
                        return current_dist + 1

                    maze[next_row][next_col] = ':('
                    queue.append([next_row, next_col, current_dist + 1])

        return -1


solution = Solution()

maze = [["+", "+", ".", "+"], [".", ".", ".", "+"], ["+", "+", "+", "."]]
entrance = [1, 2]

result = solution.nearestExit(maze, entrance)
print("Test case 1 - Expected: 1, Got:", result)

maze = [["+", "+", "+"], [".", ".", "."], ["+", "+", "+"]]
entrance = [1, 0]

result = solution.nearestExit(maze, entrance)
print("Test case 2 - Expected: 2, Got:", result)

maze = [[".", "+"]]
entrance = [0, 0]

result = solution.nearestExit(maze, entrance)
print("Test case 2 - Expected: -1, Got:", result)
