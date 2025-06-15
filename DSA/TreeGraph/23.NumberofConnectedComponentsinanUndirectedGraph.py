from collections import defaultdict
from typing import List


class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        count_components = 0
        graph = defaultdict(list)
        seen = set()

        for a, b in edges:
            graph[a].append(b)
            graph[b].append(a)

        def dfs(node):
            for adj in graph[node]:
                if adj not in seen:
                    seen.add(adj)
                    dfs(adj)

        for i in range(n):
            if i not in seen:
                count_components += 1
                seen.add(i)
                dfs(i)

        return count_components


solution = Solution()

edges = [[0, 1], [1, 2], [3, 4]]
n = 5
result = solution.countComponents(n, edges)
print("Test case 1 - Expected: 2, Got:", result)

edges = [[0, 1], [1, 2], [2, 3], [3, 4]]
n = 5
result = solution.countComponents(n, edges)
print("Test case 2 - Expected: 1, Got:", result)
