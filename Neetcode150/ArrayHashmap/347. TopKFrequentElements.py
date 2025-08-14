# LeetCode 347: Top K Frequent Elements
# https://leetcode.com/problems/top-k-frequent-elements/

from collections import Counter
import heapq


class Solution:
    def topKFrequent(self, nums, k):
        if k == len(nums):
            return nums
        
        counter = Counter(nums)
        heap = []
    
        for num, freq in counter.items():
            heapq.heappush(heap, (-freq, num))

        return [heapq.heappop(heap)[1] for _ in range(k)]


# Test cases
solution = Solution()

# Test case 1
nums1 = [1, 1, 1, 2, 2, 3]
k1 = 2
print(f"Test case 1: {solution.topKFrequent(nums1, k1)}")  # Expected: [1, 2]

# Test case 2
nums2 = [1]
k2 = 1
print(f"Test case 2: {solution.topKFrequent(nums2, k2)}")  # Expected: [1]

# Test case 3
nums3 = [1, 2]
k3 = 2
print(f"Test case 3: {solution.topKFrequent(nums3, k3)}")  # Expected: [1, 2]

# Test case 4
nums4 = [3, 0, 1, 0]
k4 = 1
print(f"Test case 4: {solution.topKFrequent(nums4, k4)}")  # Expected: [0]

# Test case 5
nums5 = [4, 1, -1, 2, -1, 2, 3]
k5 = 2
print(f"Test case 5: {solution.topKFrequent(nums5, k5)}")  # Expected: [-1, 2]
