from collections import Counter
import heapq
from typing import List



class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        if k == len(nums):
            return nums

        freq = Counter(nums)
        heap = [(-count, value) for value, count in freq.items()]

        heapq.heapify(heap)

        return [heapq.heappop(heap)[1] for i in range(k)]

# Test cases
solution = Solution()

# Test case 1: Basic test
nums1 = [1,1,1,2,2,3]
k1 = 2
result1 = solution.topKFrequent(nums1, k1)
print(f"Test case 1: {result1}")  # Expected: [1,2] (order may vary)

# Test case 2: All elements are unique
nums2 = [4,5,6,7]
k2 = 2
result2 = solution.topKFrequent(nums2, k2)
print(f"Test case 2: {result2}")  # Expected: [4,5] or any two elements

# Test case 3: k equals length of nums
nums3 = [1,2,3]
k3 = 3
result3 = solution.topKFrequent(nums3, k3)
print(f"Test case 3: {result3}")  # Expected: [1,2,3] (order may vary)

# Test case 4: Single element repeated
nums4 = [5,5,5,5]
k4 = 1
result4 = solution.topKFrequent(nums4, k4)
print(f"Test case 4: {result4}")  # Expected: [5]

# Test case 5: Negative numbers
nums5 = [-1,-1,2,2,3]
k5 = 2
result5 = solution.topKFrequent(nums5, k5)
print(f"Test case 5: {result5}")  # Expected: [-1,2] (order may vary)