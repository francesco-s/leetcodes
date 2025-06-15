from typing import List
import heapq


class Solution:

    def findKthLargest(self, nums: List[int], k: int) -> int:
        nums = [-num for num in nums]
        heapq.heapify(nums)

        for i in range(k-1):
            heapq.heappop(nums)

        return -heapq.heappop(nums)

    def findKthLargestSorting(self, nums: List[int], k: int) -> int:
        return sorted(nums)[- k]


solution = Solution()

nums = [3, 2, 1, 5, 6, 4]
k = 2

result = solution.findKthLargest(nums, k)
print("Test case 1 - Expected: 5, Got:", result)

nums = [3, 2, 3, 1, 2, 4, 5, 5, 6]
k = 4

result = solution.findKthLargest(nums, k)
print("Test case 1 - Expected: 4, Got:", result)

nums = [-1, -1]
k = 2

result = solution.findKthLargest(nums, k)
print("Test case 1 - Expected: -1, Got:", result)
