from typing import List
import math

class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        """
        Finds the minimum eating speed Koko needs to eat all bananas in h hours.

        Time Complexity: O(N * log M), where N is the number of piles and M is the max pile size.
        Space Complexity: O(1), uses constant extra space.
        """
        right = max(piles)
        left = 1

        while left < right:
            middle = left + ((right - left) // 2)
            k = 0

            for pile in piles:
                q = pile // middle
                if pile % middle != 0:
                    q += 1
                k += q
            
            if k <= h:
                right = middle
            else:
                left = middle + 1

        return right


# Test cases
solution = Solution()

# Test case 1
piles1 = [3,6,7,11]
h1 = 8
result1 = solution.minEatingSpeed(piles1, h1)
print(f"Test case 1: {result1}")  # Expected: 4

# Test case 2
piles2 = [30,11,23,4,20]
h2 = 5
result2 = solution.minEatingSpeed(piles2, h2)
print(f"Test case 2: {result2}")  # Expected: 30

# Test case 3
piles3 = [30,11,23,4,20]
h3 = 6
result3 = solution.minEatingSpeed(piles3, h3)
print(f"Test case 3: {result3}")  # Expected: 23

# Test case 4
piles4 = [1000000000]
h4 = 2
result4 = solution.minEatingSpeed(piles4, h4)
print(f"Test case 4: {result4}")  # Expected: 500000000

# Test case 5
piles5 = [312884470]
h5 = 312884469
result5 = solution.minEatingSpeed(piles5, h5)
print(f"Test case 5: {result5}")  # Expected: 2

# Test case 6
piles6 = [2,2]
h6 = 4
result6 = solution.minEatingSpeed(piles6, h6)
print(f"Test case 6: {result6}")  # Expected: 1
