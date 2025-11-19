from collections import deque


class Solution:
    def canFinish(self, numCourses, prerequisites):
        """
        :type numCourses: int
        :type prerequisites: List[List[int]]  # each [a, b] means b -> a edge
        :rtype: bool

        Time Complexity: O(V + E), where V is the number of courses and E is the number of prerequisites.
        Space Complexity: O(V + E), to store the indegree list and the adjacency list.
        """
        indegree = [0] * numCourses
        adj = [[] for _ in range(numCourses)]

        for a, b in prerequisites:
            indegree[b] += 1
            adj[a].append(b)

        q = deque()

        for i in range(numCourses):
            if indegree[i] == 0:
                q.append(i)

        finished = 0
        while q:
            course_id = q.popleft()
            finished += 1
            for neight in adj[course_id]:
                indegree[neight] -= 1
                if indegree[neight] == 0:
                    q.append(neight)

        return finished == numCourses


# Test cases
solution = Solution()

# Test case 1 (example: possible)
n1 = 2
pre1 = [[1, 0]]
res1 = solution.canFinish(n1, pre1)
print(f"Test case 1: {res1}")  # Expected: True

# Test case 2 (example: cycle)
n2 = 2
pre2 = [[1, 0], [0, 1]]
res2 = solution.canFinish(n2, pre2)
print(f"Test case 2: {res2}")  # Expected: False

# Test case 3 (branching dependencies)
n3 = 4
pre3 = [[1, 0], [2, 0], [3, 1], [3, 2]]
res3 = solution.canFinish(n3, pre3)
print(f"Test case 3: {res3}")  # Expected: True

# Test case 4 (no prerequisites)
n4 = 3
pre4 = []
res4 = solution.canFinish(n4, pre4)
print(f"Test case 4: {res4}")  # Expected: True

# Test case 5 (self-loop impossible)
n5 = 1
pre5 = [[0, 0]]
res5 = solution.canFinish(n5, pre5)
print(f"Test case 5: {res5}")  # Expected: False

# Test case 6 (disconnected cycles)
n6 = 5
pre6 = [[1, 0], [0, 1], [3, 2], [2, 3]]
res6 = solution.canFinish(n6, pre6)
print(f"Test case 6: {res6}")  # Expected: False


# Test cases
solution = Solution()

# Test case 1 (example: possible)
n1 = 2
pre1 = [[1, 0]]
res1 = solution.canFinish(n1, pre1)
print(f"Test case 1: {res1}")  # Expected: True

# Test case 2 (example: cycle)
n2 = 2
pre2 = [[1, 0], [0, 1]]
res2 = solution.canFinish(n2, pre2)
print(f"Test case 2: {res2}")  # Expected: False

# Test case 3 (branching dependencies)
n3 = 4
pre3 = [[1, 0], [2, 0], [3, 1], [3, 2]]
res3 = solution.canFinish(n3, pre3)
print(f"Test case 3: {res3}")  # Expected: True

# Test case 4 (no prerequisites)
n4 = 3
pre4 = []
res4 = solution.canFinish(n4, pre4)
print(f"Test case 4: {res4}")  # Expected: True

# Test case 5 (self-loop impossible)
n5 = 1
pre5 = [[0, 0]]
res5 = solution.canFinish(n5, pre5)
print(f"Test case 5: {res5}")  # Expected: False

# Test case 6 (disconnected cycles)
n6 = 5
pre6 = [[1, 0], [0, 1], [3, 2], [2, 3]]
res6 = solution.canFinish(n6, pre6)
print(f"Test case 6: {res6}")  # Expected: False
