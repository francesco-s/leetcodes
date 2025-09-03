import heapq

class KthLargest:

    def __init__(self, k, nums):
        """
        :type k: int
        :type nums: List[int]
        """
        self.heap = nums
        self.k = k
        heapq.heapify(self.heap)
        while len(self.heap) > k:
            heapq.heappop(self.heap)
        

    def add(self, val: int) -> int:
        if len(self.heap) < self.k or self.heap[0] < val:
            heapq.heappush(self.heap, val)

            if len(self.heap) > self.k:
                heapq.heappop(self.heap)

        return self.heap[0]
        

# Test cases
# Example 1
k1 = 3
nums1 = [4, 5, 8, 2]
kthLargest1 = KthLargest(k1, nums1)
print(kthLargest1.add(3))   # Expected: 4
print(kthLargest1.add(5))   # Expected: 5
print(kthLargest1.add(10))  # Expected: 5
print(kthLargest1.add(9))   # Expected: 8
print(kthLargest1.add(4))   # Expected: 8
print()

# Example 2
k2 = 4
nums2 = [7, 7, 7, 7, 8, 3]
kthLargest2 = KthLargest(k2, nums2)
print(kthLargest2.add(2))   # Expected: 7
print(kthLargest2.add(10))  # Expected: 7
print(kthLargest2.add(9))   # Expected: 7
print(kthLargest2.add(9))  # Expected: 8
