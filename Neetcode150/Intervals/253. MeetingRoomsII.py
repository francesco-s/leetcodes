import heapq

class Solution:

        def minMeetingRooms(self, intervals):
            """
            Time Complexity: O(n log n) - sorting takes O(n log n), and each of the n heap operations takes O(log n)
            Space Complexity: O(n) - heap can contain up to n end times in the worst case
            """
            if not intervals:
                return 0

            free_rooms = []

            intervals.sort(key=lambda x: x[0])
            heapq.heappush(free_rooms, intervals[0][1])

            for interval in intervals[1:]:
                if free_rooms[0] <= interval[0]:
                    heapq.heappop(free_rooms)

                heapq.heappush(free_rooms, interval[1])

            return len(free_rooms)
        

# Test cases
solution = Solution()

# Test case 1 (example)
intervals1 = [[0,30],[5,10],[15,20]]
res1 = solution.minMeetingRooms(intervals1)
print(f"Test case 1: {res1}")  # Expected: 2

# Test case 2 (example - no overlap)
intervals2 = [[7,10],[2,4]]
res2 = solution.minMeetingRooms(intervals2)
print(f"Test case 2: {res2}")  # Expected: 1

# Test case 3 (empty intervals)
intervals3 = []
res3 = solution.minMeetingRooms(intervals3)
print(f"Test case 3: {res3}")  # Expected: 0

# Test case 4 (single meeting)
intervals4 = [[1,5]]
res4 = solution.minMeetingRooms(intervals4)
print(f"Test case 4: {res4}")  # Expected: 1

# Test case 5 (all overlapping)
intervals5 = [[1,10],[2,7],[3,6],[4,5]]
res5 = solution.minMeetingRooms(intervals5)
print(f"Test case 5: {res5}")  # Expected: 4

# Test case 6 (sequential meetings)
intervals6 = [[1,5],[5,10],[10,15]]
res6 = solution.minMeetingRooms(intervals6)
print(f"Test case 6: {res6}")  # Expected: 1

# Test case 7 (complex overlap)
intervals7 = [[0,10],[5,15],[10,20]]
res7 = solution.minMeetingRooms(intervals7)
print(f"Test case 7: {res7}")  # Expected: 2
