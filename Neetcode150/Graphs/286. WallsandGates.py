from collections import deque
from typing import List


class Solution:
    def wallsAndGates(self, rooms: List[List[int]]) -> None:
        """
        Do not return anything, modify rooms in-place instead.

        Time Complexity: O(m * n) — each cell is enqueued and processed at most once.
        Space Complexity: O(m * n) — the queue may hold up to all cells in the worst case.
        """
        if not rooms or not rooms[0]:
            return

        ROWS, COLS = len(rooms), len(rooms[0])
        q = deque()

        for r in range(ROWS):
            for c in range(COLS):
                if rooms[r][c] == 0:
                    q.append((r, c))

        while q:
            r, c = q.popleft()
            for dr, dc in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
                nr, nc = r + dr, c + dc

                if 0 <= nr < ROWS and 0 <= nc < COLS and rooms[nr][nc] == 2147483647:
                    rooms[nr][nc] = rooms[r][c] + 1
                    q.append((nr, nc))

    def wallsAndGatesDFS(self, rooms: List[List[int]]) -> None:
        """
        Do not return anything, modify rooms in-place instead.

        Time Complexity: O(m * n) on average, but (m*n)^2. In pathological cases with many gates and repeated traversals
                         the worst-case time can be higher (upper bound depends on gate distribution).
        Space Complexity: O(m * n) worst-case recursion call stack (where m and n are the number of rows and columns).
        """
        ROWS, COLS = len(rooms), len(rooms[0])

        def dfs(r, c, steps):
            if r < 0 or r >= ROWS or c < 0 or c >= COLS or rooms[r][c] == -1:
                return

            if rooms[r][c] < steps:
                return

            rooms[r][c] = steps

            dfs(r + 1, c, steps + 1)
            dfs(r - 1, c, steps + 1)
            dfs(r, c + 1, steps + 1)
            dfs(r, c - 1, steps + 1)

        for r in range(ROWS):
            for c in range(COLS):
                if rooms[r][c] == 0:
                    dfs(r, c, 0)


# Test cases
solution = Solution()
INF = 2147483647

# Test case 1 (example)
rooms1 = [[INF, -1, 0, INF], [INF, INF, INF, -1], [INF, -1, INF, -1], [0, -1, INF, INF]]
solution.wallsAndGates(rooms1)
print(f"Test case 1: {rooms1}")
# Expected: [
#   [3, -1, 0, 1],
#   [2, 2, 1, -1],
#   [1, -1, 2, -1],
#   [0, -1, 3, 4]
# ]

# Test case 2 (only one gate)
rooms2 = [[0, INF]]
solution.wallsAndGates(rooms2)
print(f"Test case 2: {rooms2}")
# Expected: [[0, 1]]

# Test case 3 (no gates)
rooms3 = [[INF, INF], [INF, INF]]
solution.wallsAndGates(rooms3)
print(f"Test case 3: {rooms3}")
# Expected: unchanged (INF everywhere)

# Test case 4 (all walls)
rooms4 = [[-1, -1, -1]]
solution.wallsAndGates(rooms4)
print(f"Test case 4: {rooms4}")
# Expected: [[-1, -1, -1]]

# Test case 5 (mixed walls and gates)
rooms5 = [[0, -1], [INF, INF]]
solution.wallsAndGates(rooms5)
print(f"Test case 5: {rooms5}")
# Expected: [[0, -1], [1, 2]]

# Test case 6 (fully connected rooms)
rooms6 = [[0, INF, INF], [INF, INF, INF], [INF, INF, 0]]
solution.wallsAndGates(rooms6)
print(f"Test case 6: {rooms6}")
# Expected: [[0, 1, 2],
#            [1, 2, 1],
#            [2, 1, 0]]
