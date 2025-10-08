from typing import List


class UnionFind():
    def __init__(self, n):
        # Time Complexity: O(n)
        # Space Complexity: O(n)
        self.parent = [i for i in range(n)]
        self.rank = [0] * n

    def find(self, node):
        # Time Complexity: O(α(n)) per operation, nearly constant time
        # Space Complexity: O(1) (ignoring recursion stack)
        if self.parent[node] != node:
            self.parent[node] = self.find(self.parent[node])
        return self.parent[node]
    
    def union(self, u, v):
        # Time Complexity: O(α(n)) per union operation
        # Space Complexity: O(1)
        root_u = self.find(u)
        root_v = self.find(v)

        if root_u == root_v:
            return False
        
        if self.rank[root_u] < self.rank[root_v]:
            self.parent[root_u] = root_v
        elif self.rank[root_u] > self.rank[root_v]:
            self.parent[root_v] = root_u
        else:
            self.parent[root_v] = root_u
            self.rank[root_u] += 1

        return True


class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        """
        Finds a redundant connection in the graph using Union-Find.

        Time Complexity: O(n * α(n)), where n is the number of edges.
        Space Complexity: O(n), required for the Union-Find data structures.
        """
        n = len(edges)
        uf = UnionFind(n + 1)

        for u, v in edges:
            if not uf.union(u, v):
                return [u, v]
        
# Test cases
solution = Solution()

# Test case 1 (example)
edges1 = [[1,2],[1,3],[2,3]]
res1 = solution.findRedundantConnection(edges1)
print(f"Test case 1: {res1}")  # Expected: [2,3]

# Test case 2 (example larger)
edges2 = [[1,2],[2,3],[3,4],[1,4],[1,5]]
res2 = solution.findRedundantConnection(edges2)
print(f"Test case 2: {res2}")  # Expected: [1,4]

# Test case 3 (simple no redundant)
edges3 = [[1,2]]
res3 = solution.findRedundantConnection(edges3)
print(f"Test case 3: {res3}")  # Expected: []

# Test case 4 (chain plus cycle)
edges4 = [[1,2],[2,3],[3,4],[4,2]]
res4 = solution.findRedundantConnection(edges4)
print(f"Test case 4: {res4}")  # Expected: [4,2]

# Test case 5 (self-loop, if allowed)
edges5 = [[1,1]]
res5 = solution.findRedundantConnection(edges5)
print(f"Test case 5: {res5}")  # Expected: [1,1] or []

# Test case 6 (complex cycle)
edges6 = [[1,2],[2,3],[3,1],[4,5]]
res6 = solution.findRedundantConnection(edges6)
print(f"Test case 6: {res6}")  # Expected: [3,1]
