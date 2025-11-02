from collections import deque
from typing import List


class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        # Time Complexity (TC): O(n + e) where e is the number of edges,
        # because we build the adjacency list and traverse each vertex and edge once.
        # Space Complexity (SC): O(n), due to the adjacency list, visited set, and queue.
        if len(edges) > (n - 1):
            return False

        adj = [[] for _ in range(n)]
        for u, v in edges:
            adj[u].append(v)
            adj[v].append(u)

        visited = set()
        q = deque([(0, -1)])
        visited.add(0)

        while q:
            node, parent = q.popleft()
            for neight in adj[node]:
                if neight == parent:
                    continue
                if neight in visited:
                    return False
                visited.add(neight)
                q.append((neight, node))

        return len(visited) == n


# Test cases
solution = Solution()

# Test case 1 (example: valid)
n1 = 5
e1 = [[0, 1], [0, 2], [0, 3], [1, 4]]
r1 = solution.validTree(n1, e1)
print(f"Test case 1: {r1}")  # Expected: True

# Test case 2 (example: has cycle)
n2 = 5
e2 = [[0, 1], [1, 2], [2, 3], [1, 3], [1, 4]]
r2 = solution.validTree(n2, e2)
print(f"Test case 2: {r2}")  # Expected: False

# Test case 3 (edge count sanity fail)
n3 = 4
e3 = [[0, 1], [2, 3]]
r3 = solution.validTree(n3, e3)
print(f"Test case 3: {r3}")  # Expected: False

# Test case 4 (single node, no edges)
n4 = 1
e4 = []
r4 = solution.validTree(n4, e4)
print(f"Test case 4: {r4}")  # Expected: True

# Test case 5 (disconnected)
n5 = 5
e5 = [[0, 1], [2, 3], [3, 4]]
r5 = solution.validTree(n5, e5)
print(f"Test case 5: {r5}")  # Expected: False

# Test case 6 (chain graph)
n6 = 4
e6 = [[0, 1], [1, 2], [2, 3]]
r6 = solution.validTree(n6, e6)
print(f"Test case 6: {r6}")  # Expected: True
