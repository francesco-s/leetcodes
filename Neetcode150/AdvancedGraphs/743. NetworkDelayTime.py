import heapq
from collections import defaultdict
from typing import List

class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        """
        Uses Dijkstra's algorithm to determine the time it takes for a signal to travel to all nodes.
        
        Time Complexity: O((E + V) log V) ~ O(E log V), where V is the number of nodes and E is the number of edges.
        Space Complexity: O(V + E)
        """
        edges = defaultdict(list)
        for u, v, w in times:
            edges[u].append((v, w))

        minHeap = [(0, k)]
        visit = set()

        while minHeap:
            cost, node = heapq.heappop(minHeap)

            if node in visit:
                continue

            visit.add(node)

            if len(visit) == n:
                return cost

            for nei, nei_cost in edges[node]:
                if nei not in visit:
                    heapq.heappush(minHeap, (cost + nei_cost, nei))

        return -1


# Test cases
solution = Solution()

# Test case 1 (example)
times1 = [[2,1,1],[2,3,1],[3,4,1]]
n1 = 4
k1 = 2
r1 = solution.networkDelayTime(times1, n1, k1)
print(f"Test case 1: {r1}")  # Expected: 2

# Test case 2 (example)
times2 = [[1,2,1]]
n2 = 2
k2 = 1
r2 = solution.networkDelayTime(times2, n2, k2)
print(f"Test case 2: {r2}")  # Expected: 1

# Test case 3 (example - unreachable)
times3 = [[1,2,1]]
n3 = 2
k3 = 2
r3 = solution.networkDelayTime(times3, n3, k3)
print(f"Test case 3: {r3}")  # Expected: -1

# Test case 4 (single node)
times4 = []
n4 = 1
k4 = 1
r4 = solution.networkDelayTime(times4, n4, k4)
print(f"Test case 4: {r4}")  # Expected: 0

# Test case 5 (multiple paths)
times5 = [[1,2,1],[2,3,2],[1,3,4]]
n5 = 3
k5 = 1
r5 = solution.networkDelayTime(times5, n5, k5)
print(f"Test case 5: {r5}")  # Expected: 3

# Test case 6 (disconnected graph)
times6 = [[1,2,1],[3,4,1]]
n6 = 4
k6 = 1
r6 = solution.networkDelayTime(times6, n6, k6)
print(f"Test case 6: {r6}")  # Expected: -1
