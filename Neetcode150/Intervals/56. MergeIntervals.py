from typing import List


class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        """
        Merge overlapping intervals.

        Time Complexity: O(n log n) due to sorting (n = len(intervals))
        Space Complexity: O(n) extra for the output (plus O(log n) for Timsort recursion/aux)
        """
        merged = []
        intervals.sort(key=lambda x: x[0])

        for i in range(len(intervals)):
            if not merged or merged[-1][1] < intervals[i][0]:
                merged.append(intervals[i])
            else:
                merged[-1] = [
                    min(intervals[i][0], merged[-1][0]),
                    max(intervals[i][1], merged[-1][1]),
                ]

        return merged


# Test cases
solution = Solution()

# Test case 1 (example)
intervals1 = [[1, 3], [2, 6], [8, 10], [15, 18]]
res1 = solution.merge(intervals1)
print(f"Test case 1: {res1}")  # Expected: [[1,6],[8,10],[15,18]]

# Test case 2 (example - touching intervals)
intervals2 = [[1, 4], [4, 5]]
res2 = solution.merge(intervals2)
print(f"Test case 2: {res2}")  # Expected: [[1,5]]

# Test case 3 (single interval)
intervals3 = [[1, 4]]
res3 = solution.merge(intervals3)
print(f"Test case 3: {res3}")  # Expected: [[1,4]]

# Test case 4 (fully contained)
intervals4 = [[1, 4], [2, 3]]
res4 = solution.merge(intervals4)
print(f"Test case 4: {res4}")  # Expected: [[1,4]]

# Test case 5 (no overlap)
intervals5 = [[1, 2], [3, 4], [5, 6]]
res5 = solution.merge(intervals5)
print(f"Test case 5: {res5}")  # Expected: [[1,2],[3,4],[5,6]]

# Test case 6 (all merge into one)
intervals6 = [[1, 4], [2, 5], [3, 6]]
res6 = solution.merge(intervals6)
print(f"Test case 6: {res6}")  # Expected: [[1,6]]

# Test case 7 (unsorted input)
intervals7 = [[8, 10], [1, 3], [2, 6], [15, 18]]
res7 = solution.merge(intervals7)
print(f"Test case 7: {res7}")  # Expected: [[1,6],[8,10],[15,18]]
