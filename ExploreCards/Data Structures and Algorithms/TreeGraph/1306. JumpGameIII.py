from typing import List


class Solution:
    def canReachRecursive(self, arr: List[int], start: int) -> bool:
        seen = set()
        def dfs(index):
            if 0 <= index < len(arr) and arr[index] >= 0 and index not in seen:

                if arr[index] == 0:
                    return True

                seen.add(index)  # first solution using set: visited index to avoid maximum recursion depth exceeded
                # arr[index] = -arr[index]  # second solution: make the value negative to mark as visited.

                return dfs(index + arr[index]) or dfs(index - arr[index])

            return False

        return dfs(start)

    def canReach(self, arr: List[int], start: int) -> bool:
        stack = [start]

        while stack:
            index = stack.pop()
            if arr[index] == 0:
                return True
            elif arr[index] < 0:
                continue
            else:
                if 0 <= index + arr[index] < len(arr):
                    stack.append(index + arr[index])
                if 0 <= index - arr[index] < len(arr):
                    stack.append(index - arr[index])

            arr[index] = -arr[index]

        return False


solution = Solution()

arr = [4, 2, 3, 0, 3, 1, 2]
start = 5

result = solution.canReach(arr, start)
print("Test case 1 - Expected: true, Got:", result)

arr = [4, 2, 3, 0, 3, 1, 2]
start = 0

result = solution.canReach(arr, start)
print("Test case 2 - Expected: true, Got:", result)

arr = [3, 0, 2, 1, 2]
start = 2

result = solution.canReach(arr, start)
print("Test case 3 - Expected: false, Got:", result)
