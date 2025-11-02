import heapq
from typing import List


class Solution:
    def minimumEffortPath(self, heights: List[List[int]]) -> int:
        """
        Computes the minimum effort path through the grid using Dijkstra's algorithm.

        Time Complexity (TC): O(m * n * log(m * n)), where m and n are the dimensions of the grid.
        Space Complexity (SC): O(m * n), due to the use of the heap and visited set.
        """
        ROWS, COLS = len(heights), len(heights[0])
        minHeap = [[0, 0, 0]]  # [diff, row, col]
        visited = set()
        directions = [[0, 1], [0, -1], [1, 0], [-1, 0]]

        while minHeap:
            diff, row, col = heapq.heappop(minHeap)

            if row == ROWS - 1 and col == COLS - 1:
                return diff

            if (row, col) in visited:
                continue

            visited.add((row, col))

            for i, j in directions:
                new_row, new_col = row + i, col + j
                if (
                    new_row >= ROWS
                    or new_col >= COLS
                    or new_row < 0
                    or new_col < 0
                    or (new_row, new_col) in visited
                ):
                    continue

                new_diff = max(diff, abs(heights[row][col] - heights[new_row][new_col]))
                heapq.heappush(minHeap, [new_diff, new_row, new_col])


# Test cases
solution = Solution()

# Test case 1 (example)
h1 = [[1, 2, 2], [3, 8, 2], [5, 3, 5]]
r1 = solution.minimumEffortPath(h1)
print(f"Test case 1: {r1}")  # Expected: 2

# Test case 2 (example)
h2 = [[1, 2, 3], [3, 8, 4], [5, 3, 5]]
r2 = solution.minimumEffortPath(h2)
print(f"Test case 2: {r2}")  # Expected: 1

# Test case 3 (example - no effort needed)
h3 = [
    [1, 2, 1, 1, 1],
    [1, 2, 1, 2, 1],
    [1, 2, 1, 2, 1],
    [1, 2, 1, 2, 1],
    [1, 1, 1, 2, 1],
]
r3 = solution.minimumEffortPath(h3)
print(f"Test case 3: {r3}")  # Expected: 0

# Test case 4 (single cell)
h4 = [[5]]
r4 = solution.minimumEffortPath(h4)
print(f"Test case 4: {r4}")  # Expected: 0

# Test case 5 (steep mountain)
h5 = [[1, 10, 6, 7, 9, 10, 4, 9]]
r5 = solution.minimumEffortPath(h5)
print(f"Test case 5: {r5}")  # Expected: 9
