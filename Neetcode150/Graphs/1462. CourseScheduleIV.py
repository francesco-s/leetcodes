from collections import deque
from typing import List


class Solution:
    # Time Complexity: O(numCourses^2 + E * numCourses) in the worst case,
    # where E is the number of prerequisites.
    # Space Complexity: O(numCourses^2), due to the storage of prerequisite sets.
    def checkIfPrerequisite(
        self, numCourses: int, prerequisites: List[List[int]], queries: List[List[int]]
    ) -> List[bool]:
        inDegree = [0] * numCourses
        adj = [[] for _ in range(numCourses)]
        isPrereq = [set() for _ in range(numCourses)]

        for _from, to in prerequisites:
            inDegree[to] += 1
            adj[_from].append(to)

        queue = deque()
        for i in range(numCourses):
            if inDegree[i] == 0:
                queue.append(i)

        while queue:
            node = queue.popleft()
            for neight in adj[node]:
                isPrereq[neight].add(node)
                isPrereq[neight].update(isPrereq[node])
                inDegree[neight] -= 1
                if inDegree[neight] == 0:
                    queue.append(neight)

        return [u in isPrereq[v] for u, v in queries]


# Test cases
solution = Solution()

# Test case 1 (example)
n1 = 2
pre1 = [[1, 0]]
q1 = [[0, 1], [1, 0]]
r1 = solution.checkIfPrerequisite(n1, pre1, q1)
print(f"Test case 1: {r1}")  # Expected: [False, True]

# Test case 2 (no prerequisites)
n2 = 2
pre2 = []
q2 = [[1, 0], [0, 1]]
r2 = solution.checkIfPrerequisite(n2, pre2, q2)
print(f"Test case 2: {r2}")  # Expected: [False, False]

# Test case 3 (transitive)
n3 = 3
pre3 = [[1, 2], [1, 0], [2, 0]]
q3 = [[1, 0], [1, 2]]
r3 = solution.checkIfPrerequisite(n3, pre3, q3)
print(f"Test case 3: {r3}")  # Expected: [True, True]

# Test case 4 (longer chain)
n4 = 4
pre4 = [[0, 1], [1, 2], [2, 3]]
q4 = [[0, 3], [2, 1], [3, 0]]
r4 = solution.checkIfPrerequisite(n4, pre4, q4)
print(f"Test case 4: {r4}")  # Expected: [True, False, False]

# Test case 5 (diamond dependency)
n5 = 4
pre5 = [[0, 1], [0, 2], [1, 3], [2, 3]]
q5 = [[0, 3], [1, 2], [2, 1]]
r5 = solution.checkIfPrerequisite(n5, pre5, q5)
print(f"Test case 5: {r5}")  # Expected: [True, False, False]

# Test case 6 (single course)
n6 = 1
pre6 = []
q6 = [[0, 0]]
r6 = solution.checkIfPrerequisite(n6, pre6, q6)
print(f"Test case 6: {r6}")  # Expected: [False]
