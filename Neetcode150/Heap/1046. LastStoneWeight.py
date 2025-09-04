import heapq
from typing import List

class Solution:

    def lastStoneWeight(self, stones: List[int]) -> int:
        """
        Returns the weight of the last remaining stone (or 0 if none remain) after repeatedly smashing the two heaviest stones.

        Time Complexity: O(n log n), where n is the number of stones.
            - Each heappush and heappop operation takes O(log n) time.
            - In the worst case, we perform O(n) such operations.

        Space Complexity: O(n)
            - We use a heap to store all stones, which requires O(n) space.
        """
        heap = []
        for x in stones:
            heapq.heappush(heap, -x)
        
        while len(heap) > 1:
            stone1 = -heapq.heappop(heap)
            stone2 = -heapq.heappop(heap)

            if stone1 != stone2:
                heapq.heappush(heap, -(stone1 - stone2))

            if not heap:
                heap = [0]

        return -heapq.heappop(heap)

# Test cases
solution = Solution()

# Test case 1 (example)
stones1 = [2,7,4,1,8,1]
res1 = solution.lastStoneWeight(stones1)
print(f"Test case 1: {res1}")  # Expected: 1

# Test case 2 (single stone)
stones2 = [1]
res2 = solution.lastStoneWeight(stones2)
print(f"Test case 2: {res2}")  # Expected: 1

# Test case 3 (all equal pairs)
stones3 = [2,2,2,2]
res3 = solution.lastStoneWeight(stones3)
print(f"Test case 3: {res3}")  # Expected: 0

# Test case 4 (mixed, ends with zero)
stones4 = [10,4,2,10]
res4 = solution.lastStoneWeight(stones4)
print(f"Test case 4: {res4}")  # Expected: 2

# Test case 5 (already descending)
stones5 = [9,8,7,6,5]
res5 = solution.lastStoneWeight(stones5)
print(f"Test case 5: {res5}")  # Expected: 1

# Test case 6 (large values)
stones6 = [31,26,33,21,40]
res6 = solution.lastStoneWeight(stones6)
print(f"Test case 6: {res6}")  # Expected: 5
