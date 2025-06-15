class Solution:
    def minMeetingRooms(self, intervals):
        start_timings = sorted([i[0] for i in intervals])
        end_timings = sorted([i[1] for i in intervals])
        
        num_rooms = 0
        i = 0
        j = 0
        
        while i < len(intervals):
            if start_timings[i] < end_timings[j]:
                num_rooms += 1
            else:
                j += 1
            i += 1
        
        return num_rooms


# Test cases
solution = Solution()

# Test case 1
intervals1 = [[0, 30], [5, 10], [15, 20]]
print("Test case 1:", solution.minMeetingRooms(intervals1))  # Expected: 2

# Test case 2
intervals2 = [[7, 10], [2, 4]]
print("Test case 2:", solution.minMeetingRooms(intervals2))  # Expected: 1

# Test case 3
intervals3 = [[5,8],[6,8]]
print("Test case 3:", solution.minMeetingRooms(intervals3))  # Expected: 2

# Test case 4
intervals4 = [[13,15],[1,13]]
print("Test case 4:", solution.minMeetingRooms(intervals4))  # Expected: 1

# Test case 5
intervals5 = [[13,15],[1,13],[6,9]]
print("Test case 5:", solution.minMeetingRooms(intervals5))  # Expected: 2