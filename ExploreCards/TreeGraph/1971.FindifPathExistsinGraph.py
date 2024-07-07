from collections import defaultdict
from typing import List


class Solution:

    def validPath(self, n: int, edges: List[List[int]], source: int, destination: int) -> bool:
        if source == destination:
            return True

        graph = defaultdict(list)
        for a, b in edges:
            graph[a].append(b)
            graph[b].append(a)

        stack = [source]
        seen = set([source])

        while stack:
            curr_node = stack.pop()
            if curr_node == destination:
                return True
            for neighbor in graph[curr_node]:
                if neighbor not in seen:
                    seen.add(neighbor)
                    stack.append(neighbor)

        return False

    def validPathDFSRec(self, n: int, edges: List[List[int]], source: int, destination):
        graph = defaultdict(list)
        for a, b in edges:
            graph[a].append(b)
            graph[b].append(a)

        seen = [False] * n

        def dfs(curr_node):
            if curr_node == destination:
                return True

            if not seen[curr_node]:
                seen[curr_node] = True
                for next_node in graph[curr_node]:
                    if dfs(next_node):
                        return True
            return False

        return dfs(source)


n = 3
edges = [[0, 1], [1, 2], [2, 0]]
source = 0
destination = 2

solution = Solution()

result = solution.validPath(n, edges, source, destination)

print("Output:", result)
