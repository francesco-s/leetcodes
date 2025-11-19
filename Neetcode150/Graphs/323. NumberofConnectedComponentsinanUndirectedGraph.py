from typing import List

# Union-Find Data Structure with Time and Space Complexity Analysis
#
# Time Complexity:
#   Initialization: O(n)
#   Each find/union: O(α(n)), where α(n) is the inverse Ackermann function (almost constant).
#   Overall for countComponents: O((n + m) * α(n)), where m is the number of edges.
#
# Space Complexity:
#   O(n) for the parent and rank arrays.


class UnionFind:
    def __init__(self, n):
        self.parent = [i for i in range(n)]
        self.rank = [0] * n

    def find(self, node):
        if self.parent[node] != node:
            self.parent[node] = self.find(self.parent[node])
        return self.parent[node]

    def union(self, u, v):
        root_u = self.find(u)
        root_v = self.find(v)

        if root_u == root_v:
            return False

        if self.rank[root_u] < self.rank[root_v]:
            self.parent[root_u] = root_v
        elif self.rank[root_v] < self.rank[root_u]:
            self.parent[root_v] = root_u
        else:
            self.parent[root_v] = root_u
            self.rank[root_u] += 1

        return True


class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        dsu = UnionFind(n)
        res = n
        for u, v in edges:
            if dsu.union(u, v):
                res -= 1
        return res


# Test cases
solution = Solution()

# Test case 1 (example)
n1 = 5
edges1 = [[0, 1], [1, 2], [3, 4]]
res1 = solution.countComponents(n1, edges1)
print(f"Test case 1: {res1}")  # Expected: 2

# Test case 2 (no edges)
n2 = 4
edges2 = []
res2 = solution.countComponents(n2, edges2)
print(f"Test case 2: {res2}")  # Expected: 4

# Test case 3 (single component)
n3 = 4
edges3 = [[0, 1], [1, 2], [2, 3]]
res3 = solution.countComponents(n3, edges3)
print(f"Test case 3: {res3}")  # Expected: 1

# Test case 4 (disconnected pairs)
n4 = 6
edges4 = [[0, 1], [2, 3], [4, 5]]
res4 = solution.countComponents(n4, edges4)
print(f"Test case 4: {res4}")  # Expected: 3

# Test case 5 (complex graph)
n5 = 7
edges5 = [[0, 1], [1, 2], [3, 4], [4, 5], [5, 6]]
res5 = solution.countComponents(n5, edges5)
print(f"Test case 5: {res5}")  # Expected: 2

# Test case 6 (single node)
n6 = 1
edges6 = []
res6 = solution.countComponents(n6, edges6)
print(f"Test case 6: {res6}")  # Expected: 1
