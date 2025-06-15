from typing import List
import heapq


class Solution:
    def minStoneSum(self, piles: List[int], k: int) -> int:
        piles = [-pile for pile in piles]
        heapq.heapify(piles)
        while k > 0:
            heapq.heappush(piles, heapq.heappop(piles) // 2)
            k -= 1

        return -sum(piles)



solution = Solution()

piles = [5, 4, 9]
k = 2

result = solution.minStoneSum(piles, k)
print("Test case 1 - Expected: 12, Got:", result)
