class Solution:
    def canAttendMeetings(self, intervals):
        if not intervals:
            return True

        intervals.sort(key=lambda x: x[0])
        prev = intervals[0]

        for interval in intervals[1:]:
            if prev[1] > interval[0]:
                return False
            prev = interval

        return True


# Test cases
solution = Solution()

# Test case 1 (example - has overlap)
intervals1 = [[0, 30], [5, 10], [15, 20]]
res1 = solution.canAttendMeetings(intervals1)
print(f"Test case 1: {res1}")  # Expected: False

# Test case 2 (example - no overlap)
intervals2 = [[7, 10], [2, 4]]
res2 = solution.canAttendMeetings(intervals2)
print(f"Test case 2: {res2}")  # Expected: True

# Test case 3 (empty intervals)
intervals3 = []
res3 = solution.canAttendMeetings(intervals3)
print(f"Test case 3: {res3}")  # Expected: True

# Test case 4 (single meeting)
intervals4 = [[1, 5]]
res4 = solution.canAttendMeetings(intervals4)
print(f"Test case 4: {res4}")  # Expected: True

# Test case 5 (adjacent meetings - no overlap)
intervals5 = [[1, 5], [5, 10], [10, 15]]
res5 = solution.canAttendMeetings(intervals5)
print(f"Test case 5: {res5}")  # Expected: True

# Test case 6 (touching at boundary)
intervals6 = [[0, 8], [8, 10]]
res6 = solution.canAttendMeetings(intervals6)
print(f"Test case 6: {res6}")  # Expected: True

# Test case 7 (multiple overlaps)
intervals7 = [[1, 5], [2, 6], [3, 7]]
res7 = solution.canAttendMeetings(intervals7)
print(f"Test case 7: {res7}")  # Expected: False
