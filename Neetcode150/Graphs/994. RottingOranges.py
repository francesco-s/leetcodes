from collections import deque
from typing import List


class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        """
        Time Complexity: O(R * C) where R = number of rows and C = number of columns.
        Every cell is visited at most once.
        Space Complexity: O(R * C) in the worst case for the queue (plus O(1) extra space).
        """
        ROWS, COLS = len(grid), len(grid[0])
        fresh = 0
        q = deque()

        for i in range(ROWS):
            for j in range(COLS):
                if grid[i][j] == 1:
                    fresh += 1
                elif grid[i][j] == 2:
                    q.append((i, j))

        q.append((-1, -1))  # To divide every BFS "level"
        directions = [[0, 1], [0, -1], [1, 0], [-1, 0]]
        minutes = -1

        while q:
            curr_i, curr_j = q.popleft()
            if curr_i == -1:  # To divide every BFS "level"
                minutes += 1
                if q:
                    q.append((-1, -1))
            else:
                for i, j in directions:
                    next_i, next_j = curr_i + i, curr_j + j
                    if (
                        0 <= next_i < ROWS
                        and 0 <= next_j < COLS
                        and grid[next_i][next_j] == 1
                    ):
                        grid[next_i][next_j] = 2
                        fresh -= 1
                        q.append((next_i, next_j))

        return minutes if fresh == 0 else -1

    def orangesRotting(self, grid: List[List[int]]) -> int:
        ROWS, COLS = len(grid), len(grid[0])
        fresh = 0
        q = deque()

        for i in range(ROWS):
            for j in range(COLS):
                if grid[i][j] == 1:
                    fresh += 1
                elif grid[i][j] == 2:
                    q.append((i, j))

        directions = [[0, 1], [0, -1], [1, 0], [-1, 0]]
        minutes = 0

        while fresh > 0 and q:
            length = len(q)
            for _ in range(length):  # Process the level
                curr_i, curr_j = q.popleft()
                for i, j in directions:
                    next_i, next_j = curr_i + i, curr_j + j
                    if (
                        0 <= next_i < ROWS
                        and 0 <= next_j < COLS
                        and grid[next_i][next_j] == 1
                    ):
                        grid[next_i][next_j] = 2
                        fresh -= 1
                        q.append((next_i, next_j))
            minutes += 1

        return minutes if fresh == 0 else -1


# Test cases
solution = Solution()

# Test case 1 (example)
grid1 = [[2, 1, 1], [1, 1, 0], [0, 1, 1]]
res1 = solution.orangesRotting(grid1)
print(f"Test case 1: {res1}")  # Expected: 4

# Test case 2 (isolated orange)
grid2 = [[2, 1, 1], [0, 1, 1], [1, 0, 1]]
res2 = solution.orangesRotting(grid2)
print(f"Test case 2: {res2}")  # Expected: -1

# Test case 3 (no fresh oranges)
grid3 = [[0, 2]]
res3 = solution.orangesRotting(grid3)
print(f"Test case 3: {res3}")  # Expected: 0

# Test case 4 (all rotten already)
grid4 = [[2, 2], [2, 2]]
res4 = solution.orangesRotting(grid4)
print(f"Test case 4: {res4}")  # Expected: 0

# Test case 5 (no rotten ones present)
grid5 = [[1, 1, 1], [1, 1, 1], [1, 1, 1]]
res5 = solution.orangesRotting(grid5)
print(f"Test case 5: {res5}")  # Expected: -1

# Test case 6 (single orange)
grid6 = [[1]]
res6 = solution.orangesRotting(grid6)
print(f"Test case 6: {res6}")  # Expected: -1
