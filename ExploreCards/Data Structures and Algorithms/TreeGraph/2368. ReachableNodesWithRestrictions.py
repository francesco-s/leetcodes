from collections import defaultdict
from typing import List


class Solution:
        def reachableNodes(self, n: int, edges: List[List[int]], restricted: List[int]) -> int:
            graph = defaultdict(list)
            restricted_set = set(restricted)

            # Create the graph
            for a, b in edges:
                graph[a].append(b)
                graph[b].append(a)

            # Initialize the stack with the starting node 0 if it is not restricted
            if 0 in restricted_set:
                return 0

            stack = [0]
            seen = {0}
            counter = 1

            while stack:
                curr_node = stack.pop()
                for neighbor in graph[curr_node]:
                    if neighbor not in seen and neighbor not in restricted_set:
                        seen.add(neighbor)
                        stack.append(neighbor)
                        counter += 1

            return counter


solution = Solution()

edges = [[0, 1], [1, 2], [3, 1], [4, 0], [0, 5], [5, 6]]
restricted = [4, 5]
n = 7
result = solution.reachableNodes(n, edges, restricted)
print("Output:", result)

edges = [[0, 1], [0, 2], [0, 5], [0, 4], [3, 2], [6, 5]]
restricted = [4, 2, 1]
n = 7
result = solution.reachableNodes(n, edges, restricted)
print("Output:", result)

edges = [[8, 2], [2, 5], [5, 0], [2, 7], [1, 7], [3, 8], [0, 4], [3, 9], [1, 6]]
restricted = [9, 8, 4, 5, 3, 1]
n = 10
result = solution.reachableNodes(n, edges, restricted)
print("Output:", result)
