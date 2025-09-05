from heapq import heappop, heappush
from typing import List


class Solution:
    #TODO: use quicksort for O(n) time

    def findKthLargest(self, nums: List[int], k: int) -> int:
        """
        Find the kth largest element in an array using a max-heap.

        Time Complexity (TC): O(n + k log n)
            - Building the heap: O(n)
            - Extracting k elements: O(k log n)
            - Overall: O(n + k log n), but since we push all elements, it's O(n log n) in this implementation.

        Space Complexity (SC): O(n)
            - The heap stores all n elements.

        Args:
            nums (List[int]): The input array.
            k (int): The kth position to find.

        Returns:
            int: The kth largest element.
        """
        max_heap = []

        for num in nums:
            heappush(max_heap, -num)

        while k > 0:
            k_largest = heappop(max_heap) 
            k -= 1

        return -k_largest

# Test cases
solution = Solution()

# Test case 1 (example)
nums1 = [3,2,1,5,6,4]
k1 = 2
res1 = solution.findKthLargest(nums1, k1)
print(f"Test case 1: {res1}")  # Expected: 5

# Test case 2 (example)
nums2 = [3,2,3,1,2,4,5,5,6]
k2 = 4
res2 = solution.findKthLargest(nums2, k2)
print(f"Test case 2: {res2}")  # Expected: 4

# Test case 3 (k = 1 -> max)
nums3 = [7,7,7]
k3 = 1
res3 = solution.findKthLargest(nums3, k3)
print(f"Test case 3: {res3}")  # Expected: 7

# Test case 4 (k = n -> min)
nums4 = [9, -1, 0, 3]
k4 = 4
res4 = solution.findKthLargest(nums4, k4)
print(f"Test case 4: {res4}")  # Expected: -1

# Test case 5 (negatives and duplicates)
nums5 = [-2, -1, -1, -3, 0, 2]
k5 = 3
res5 = solution.findKthLargest(nums5, k5)
print(f"Test case 5: {res5}")  # Expected: -1

# Test case 6 (large k in mixed array)
nums6 = [10, 100, 50, 50, 5, 20]
k6 = 5
res6 = solution.findKthLargest(nums6, k6)
print(f"Test case 6: {res6}")  # Expected: 10
