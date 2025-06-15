from typing import List
import heapq


class Solution:
    def connectSticks(self, sticks: List[int]) -> int:
        heapq.heapify(sticks)
        cum_cost = 0
        while len(sticks) > 1:
            first = heapq.heappop(sticks)
            sec = heapq.heappop(sticks)
            cost = first + sec
            heapq.heappush(sticks, cost)
            cum_cost += cost

        return cum_cost



solution = Solution()

sticks = [2, 4, 3]

result = solution.connectSticks(sticks)
print("Test case 1 - Expected: 14, Got:", result)

sticks = [1,8,3,5]

result = solution.connectSticks(sticks)
print("Test case 1 - Expected: 30, Got:", result)

