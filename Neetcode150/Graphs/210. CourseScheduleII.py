from collections import deque


class Solution:
    def findOrder(self, numCourses, prerequisites):
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

        res = []

        while q:
            course_id = q.popleft()
            res.append(course_id)
            for neight in adj[course_id]:
                indegree[neight] -= 1
                if indegree[neight] == 0:
                    q.append(neight)

        return res[::-1] if len(res) == numCourses else []


# Test cases
solution = Solution()

# Test case 1 (example)
n1 = 2
pre1 = [[1, 0]]
res1 = solution.findOrder(n1, pre1)
print(f"Test case 1: {res1}")  # Expected: [0,1]

# Test case 2 (example with branching)
n2 = 4
pre2 = [[1, 0], [2, 0], [3, 1], [3, 2]]
res2 = solution.findOrder(n2, pre2)
print(f"Test case 2: {res2}")  # Expected: [0,1,2,3] or [0,2,1,3]

# Test case 3 (cycle -> empty)
n3 = 2
pre3 = [[1, 0], [0, 1]]
res3 = solution.findOrder(n3, pre3)
print(f"Test case 3: {res3}")  # Expected: []

# Test case 4 (no prerequisites)
n4 = 3
pre4 = []
res4 = solution.findOrder(n4, pre4)
print(f"Test case 4: {res4}")  # Expected: any permutation of [0,1,2]

# Test case 5 (single course)
n5 = 1
pre5 = []
res5 = solution.findOrder(n5, pre5)
print(f"Test case 5: {res5}")  # Expected: [0]

# Test case 6 (disconnected DAG components)
n6 = 6
pre6 = [[2, 1], [3, 2], [5, 4]]
res6 = solution.findOrder(n6, pre6)
print(
    f"Test case 6: {res6}"
)  # Expected: a topo order like [0,1,2,3,4,5] or [4,5,0,1,2,3], etc.
