from collections import Counter
from typing import List

class Solution:

    def isNStraightHand(self, hand, groupSize):
        """
        Determine if hand can be arranged into groups of consecutive cards of size groupSize.

        Time Complexity: O(n log n), where n = len(hand) (sorting dominates).
        Space Complexity: O(n), for the Counter and sorting overhead.
        """
        if len(hand) % groupSize:
            return False

        count = Counter(hand)
        hand.sort()

        for num in hand:
            if count[num]:
                for i in range(num, num + groupSize):
                    if not count[i]:
                        return False
                    count[i] -= 1

        return True

    def isNStraightHand(self, hand: List[int], groupSize: int) -> bool:
        """
        Determine if hand can be arranged into groups of consecutive cards of size groupSize.

        Time Complexity: O(n * groupSize) worst-case, where n = len(hand).
        Space Complexity: O(n) for the Counter and temporary bookkeeping.
        """
        if len(hand) % groupSize:
            return False

        count = Counter(hand)
        for num in hand:
            start = num
            while count[start - 1]:
                start -= 1
            while start <= num:
                while count[start]:
                    for i in range(start, start + groupSize):
                        if not count[i]:
                            return False
                        count[i] -= 1
                start += 1

        return True

    

# Test cases
solution = Solution()

# Test case 1 (example)
hand1 = [1,2,3,6,2,3,4,7,8]
groupSize1 = 3
res1 = solution.isNStraightHand(hand1, groupSize1)
print(f"Test case 1: {res1}")  # Expected: True

# Test case 2 (example - impossible)
hand2 = [1,2,3,4,5]
groupSize2 = 4
res2 = solution.isNStraightHand(hand2, groupSize2)
print(f"Test case 2: {res2}")  # Expected: False

# Test case 3 (example - pair)
hand3 = [2,1]
groupSize3 = 2
res3 = solution.isNStraightHand(hand3, groupSize3)
print(f"Test case 3: {res3}")  # Expected: True

# Test case 4 (single group)
hand4 = [1,2,3,4,5]
groupSize4 = 5
res4 = solution.isNStraightHand(hand4, groupSize4)
print(f"Test case 4: {res4}")  # Expected: True

# Test case 5 (gap in sequence)
hand5 = [1,2,4,5]
groupSize5 = 2
res5 = solution.isNStraightHand(hand5, groupSize5)
print(f"Test case 5: {res5}")  # Expected: True

# Test case 6 (length not divisible)
hand6 = [1,2,3,4,5,6,7]
groupSize6 = 3
res6 = solution.isNStraightHand(hand6, groupSize6)
print(f"Test case 6: {res6}")  # Expected: False
