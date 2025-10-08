from typing import List


class UnionFind():
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
        elif self.rank[root_u] > self.rank[root_v]:
            self.parent[root_v] = root_u
        else:
            self.parent[root_v] = root_u
            self.rank[root_u] += 1

        return True

class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        """
        Use Kruskal's algorithm with Union-Find to build a Minimum Spanning Tree (MST).
        
        Time Complexity:
            O(n^2 log n), where n is the number of points. We have O(n^2) edges being sorted.
        Space Complexity:
            O(n^2), for storing all pairwise edges.
        """
        n = len(points)
        all_edges = []
        
        for curr in range(n): 
            for _next in range(curr + 1, n): 
                w = abs(points[curr][0] - points[_next][0]) + abs(points[curr][1] - points[_next][1])
                all_edges.append((w, curr, _next))

        all_edges.sort()
        uf = UnionFind(n)
        total_w = 0
        edge_used = 0

        for w, u, v in all_edges:
            if uf.union(u, v):
                total_w += w
                edge_used += 1
                if edge_used == n - 1:
                    return total_w

        return total_w



        

# Test cases
solution = Solution()

# Test case 1 (example)
points1 = [[0,0],[2,2],[3,10],[5,2],[7,0]]
res1 = solution.minCostConnectPoints(points1)
print(f"Test case 1: {res1}")  # Expected: 20

# Test case 2 (two points)
points2 = [[3,12],[-2,5],[-4,1]]
res2 = solution.minCostConnectPoints(points2)
print(f"Test case 2: {res2}")  # Expected: 18

# Test case 3 (single point)
points3 = [[0,0]]
res3 = solution.minCostConnectPoints(points3)
print(f"Test case 3: {res3}")  # Expected: 0

# Test case 4 (collinear points)
points4 = [[1,1],[2,2],[3,3]]
res4 = solution.minCostConnectPoints(points4)
print(f"Test case 4: {res4}")  # Expected: 4

# Test case 5 (square)
points5 = [[0,0],[0,1],[1,0],[1,1]]
res5 = solution.minCostConnectPoints(points5)
print(f"Test case 5: {res5}")  # Expected: 3
