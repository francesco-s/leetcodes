class Solution:
    def allPathsSourceTarget(self, graph: list[list[int]]) -> list[list[int]]:
        target = len(graph) - 1
        results = []

        def backtracking(curr_node, path):
            if curr_node == target:
                results.append(list(path))
                return
            
            for next_node in graph[curr_node]:
                path.append(next_node)
                backtracking(next_node, path)
                path.pop()


        path = [0]
        backtracking(0, path)

        return results


# Test cases
solution = Solution()

# Test case 1
graph1 = [[1, 2], [3], [3], []]
print("Test case 1:", solution.allPathsSourceTarget(graph1))  # Expected: [[0, 1, 3], [0, 2, 3]]

graph2 = [[4, 3, 1], [3, 2, 4], [3], [4], []]
print("Test case 2:", solution.allPathsSourceTarget(graph2))  # Expected: [[0, 4], [0, 3, 4], [0, 1, 3, 4], [0, 1, 2, 3, 4], [0, 1, 4]]