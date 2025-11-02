class Solution:

    def eraseOverlapIntervals(self, intervals):
        """
        Time Complexity: O(n log n) due to sorting
        Space Complexity: O(1) extra space (ignoring input)
        """
        if not intervals:
            return 0

        intervals.sort(key=lambda x: x[1])
        res = 0
        prevEnd = intervals[0][1]

        for start, end in intervals[1:]:
            if start >= prevEnd:
                prevEnd = end
            else:
                res += 1
                prevEnd = min(prevEnd, end)

        return res

# Test cases
solution = Solution()

# Test case 1 (example)
intervals1 = [[1,2],[2,3],[3,4],[1,3]]
res1 = solution.eraseOverlapIntervals(intervals1)
print(f"Test case 1: {res1}")  # Expected: 1

# Test case 2 (example - all same)
intervals2 = [[1,2],[1,2],[1,2]]
res2 = solution.eraseOverlapIntervals(intervals2)
print(f"Test case 2: {res2}")  # Expected: 2

# Test case 3 (example - no overlap)
intervals3 = [[1,2],[2,3]]
res3 = solution.eraseOverlapIntervals(intervals3)
print(f"Test case 3: {res3}")  # Expected: 0

# Test case 4 (single interval)
intervals4 = [[1,2]]
res4 = solution.eraseOverlapIntervals(intervals4)
print(f"Test case 4: {res4}")  # Expected: 0

# Test case 5 (nested intervals)
intervals5 = [[1,100],[11,22],[1,11],[2,12]]
res5 = solution.eraseOverlapIntervals(intervals5)
print(f"Test case 5: {res5}")  # Expected: 2

# Test case 6 (chain overlap)
intervals6 = [[1,3],[2,4],[3,5],[4,6]]
res6 = solution.eraseOverlapIntervals(intervals6)
print(f"Test case 6: {res6}")  # Expected: 2
