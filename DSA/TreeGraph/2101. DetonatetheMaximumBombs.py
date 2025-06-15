from collections import defaultdict
from typing import List


class Solution:

    def maximumDetonation(self, bombs: List[List[int]]) -> int:
        graph = defaultdict(list)

        # for i, (x1, y1, ri) in enumerate(bombs):
        #     for j, (x2, y2, _) in enumerate(bombs):
        #         if x1 == x2 and y1 == y2:
        #             continue
        #         if ri ** 2 >= (x1 - x2) ** 2 + (y1 - y2) ** 2:
        #             graph[i].append(j)

        # Optimized code
        for i, (x1, y1, r1) in enumerate(bombs):
            r1_squared = r1 ** 2
            for j in range(i + 1, len(bombs)):
                x2, y2, _ = bombs[j]
                distance_squared = (x1 - x2) ** 2 + (y1 - y2) ** 2
                if r1_squared >= distance_squared:
                    graph[i].append(j)
                if bombs[j][2] ** 2 >= distance_squared:
                    graph[j].append(i)

        print(graph)

        def dfs_rec(curr, seen):
            seen.add(curr)
            for bomb in graph[curr]:
                if bomb not in seen:
                    dfs_rec(bomb, seen)

            return len(seen)

        def dfs(i):
            stack = [i]
            seen = set([i])
            while stack:
                bomb_to_explode = stack.pop()
                for bomb in graph[bomb_to_explode]:
                    if bomb not in seen:
                        seen.add(bomb)
                        stack.append(bomb)
            return len(seen)

        answer = 0
        # for i in range(len(bombs)):
        #     answer = max(answer, dfs(i))

        for i in range(len(bombs)):
            answer = max(answer, dfs_rec(i, set()))

        return answer


solution = Solution()

bombs = [[2, 1, 3], [6, 1, 4]]

result = solution.maximumDetonation(bombs)
print("Test case 1 - Expected: 2, Got:", result)

bombs = [[1, 1, 5], [10, 10, 5]]

result = solution.maximumDetonation(bombs)
print("Test case 2 - Expected: 1, Got:", result)

bombs = [[1, 2, 3], [2, 3, 1], [3, 4, 2], [4, 5, 3], [5, 6, 4]]

result = solution.maximumDetonation(bombs)
print("Test case 3 - Expected: 5, Got:", result)
