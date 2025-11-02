import heapq
from typing import List


class Solution:
    def findCheapestPrice(
        self, n: int, flights: List[List[int]], src: int, dst: int, k: int
    ) -> int:
        """
        Finds the cheapest flight from src to dst with at most k stops.

        Time Complexity (TC): O((k+1) * E * log(n*(k+1)))
            - There are O(n*(k+1)) possible states (each node with stops count ranging from 0 to k+1).
            - Each state can be pushed to the min heap, and each push/pop takes O(log(n*(k+1))).
            - In the worst-case, we explore each flight from each state.
        Space Complexity (SC): O(n*(k+1))
            - We maintain a distance table of size n*(k+2) (effectively O(n*(k+1))) and a min heap with similar size.
        """
        adj = [[] for _ in range(n)]
        for u, v, cost in flights:
            adj[u].append([v, cost])

        dist = [[float("inf")] * (k + 2) for _ in range(n)]
        dist[src][0] = 0
        min_heap = [(0, src, -1)]

        while min_heap:
            cost, node, stops = heapq.heappop(min_heap)
            if dst == node:
                return cost
            if stops == k or dist[node][stops + 1] < cost:
                continue

            for nei, w in adj[node]:
                new_cost = w + cost
                new_stops = stops + 1
                if dist[nei][new_stops + 1] > new_cost:
                    dist[nei][new_stops + 1] = new_cost
                    heapq.heappush(min_heap, (new_cost, nei, new_stops))

        return -1


# Test cases
solution = Solution()

# Test case 1 (example)
n1 = 3
flights1 = [[0, 1, 100], [1, 2, 100], [0, 2, 500]]
src1, dst1, k1 = 0, 2, 1
res1 = solution.findCheapestPrice(n1, flights1, src1, dst1, k1)
print(f"Test case 1: {res1}")  # Expected: 200

# Test case 2 (example, K too small)
n2 = 3
flights2 = [[0, 1, 100], [1, 2, 100], [0, 2, 500]]
src2, dst2, k2 = 0, 2, 0
res2 = solution.findCheapestPrice(n2, flights2, src2, dst2, k2)
print(f"Test case 2: {res2}")  # Expected: 500

# Test case 3 (no possible route)
n3 = 4
flights3 = [[0, 1, 1], [1, 2, 1], [2, 3, 1], [0, 3, 10]]
src3, dst3, k3 = 0, 3, 1
res3 = solution.findCheapestPrice(n3, flights3, src3, dst3, k3)
print(f"Test case 3: {res3}")  # Expected: 10

# Test case 4 (multi-branch, must pick cheapest within stops)
n4 = 4
flights4 = [[0, 1, 1], [0, 2, 5], [1, 2, 1], [2, 3, 1]]
src4, dst4, k4 = 0, 3, 1
res4 = solution.findCheapestPrice(n4, flights4, src4, dst4, k4)
print(f"Test case 4: {res4}")  # Expected: 6

# Test case 5 (only route is too long)
n5 = 3
flights5 = [[0, 1, 1], [1, 2, 1], [0, 2, 100]]
src5, dst5, k5 = 0, 2, 0
res5 = solution.findCheapestPrice(n5, flights5, src5, dst5, k5)
print(f"Test case 5: {res5}")  # Expected: 100

# Test case 6 (source equals destination)
n6 = 3
flights6 = [[0, 1, 100], [1, 2, 100], [0, 2, 500]]
src6, dst6, k6 = 1, 1, 1
res6 = solution.findCheapestPrice(n6, flights6, src6, dst6, k6)
print(f"Test case 6: {res6}")  # Expected: 0
