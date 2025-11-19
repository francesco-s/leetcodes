from typing import List


class Solution:
    def insert(
        self, intervals: List[List[int]], newInterval: List[int]
    ) -> List[List[int]]:
        """
        Insert newInterval into a list of non-overlapping, sorted intervals and merge overlaps.

        Time Complexity: O(n) — single pass through the intervals list.
        Space Complexity: O(n) — output list may contain up to n+1 intervals (O(1) extra auxiliary space).
        """
        res = []

        for i in range(len(intervals)):
            if newInterval[1] < intervals[i][0]:
                res.append(newInterval)
                return res + intervals[i:]
            elif newInterval[0] > intervals[i][1]:
                res.append(intervals[i])
            else:
                newInterval = [
                    min(newInterval[0], intervals[i][0]),
                    max(newInterval[1], intervals[i][1]),
                ]
        res.append(newInterval)
        return res


# Test cases
solution = Solution()

# Test case 1 (example)
intervals1 = [[1, 3], [6, 9]]
newInterval1 = [2, 5]
res1 = solution.insert(intervals1, newInterval1)
print(f"Test case 1: {res1}")  # Expected: [[1,5],[6,9]]

# Test case 2 (example - multiple merges)
intervals2 = [[1, 2], [3, 5], [6, 7], [8, 10], [12, 16]]
newInterval2 = [4, 8]
res2 = solution.insert(intervals2, newInterval2)
print(f"Test case 2: {res2}")  # Expected: [[1,2],[3,10],[12,16]]

# Test case 3 (empty intervals)
intervals3 = []
newInterval3 = [5, 7]
res3 = solution.insert(intervals3, newInterval3)
print(f"Test case 3: {res3}")  # Expected: [[5,7]]

# Test case 4 (no overlap - insert at beginning)
intervals4 = [[3, 5], [6, 9]]
newInterval4 = [1, 2]
res4 = solution.insert(intervals4, newInterval4)
print(f"Test case 4: {res4}")  # Expected: [[1,2],[3,5],[6,9]]

# Test case 5 (no overlap - insert at end)
intervals5 = [[1, 2], [3, 5]]
newInterval5 = [6, 8]
res5 = solution.insert(intervals5, newInterval5)
print(f"Test case 5: {res5}")  # Expected: [[1,2],[3,5],[6,8]]

# Test case 6 (covers all intervals)
intervals6 = [[1, 2], [3, 4], [5, 6]]
newInterval6 = [0, 7]
res6 = solution.insert(intervals6, newInterval6)
print(f"Test case 6: {res6}")  # Expected: [[0,7]]

# Test case 7 (insert in middle without overlap)
intervals7 = [[1, 2], [5, 6]]
newInterval7 = [3, 4]
res7 = solution.insert(intervals7, newInterval7)
print(f"Test case 7: {res7}")  # Expected: [[1,2],[3,4],[5,6]]
