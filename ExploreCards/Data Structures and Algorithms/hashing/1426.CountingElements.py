from typing import List


# Example 1:
#
# Input: arr = [1,2,3]
# Output: 2
# Explanation: 1 and 2 are counted cause 2 and 3 are in arr.
#
# Example 2:
#
# Input: arr = [1,1,3,3,5,5,7,7]
# Output: 0
# Explanation: No numbers are counted, cause there is no 2, 4, 6, or 8 in arr.

class Solution:
    def countElements(arr: List[int]) -> int:
        hashset = set(arr)
        count = 0

        for x in arr:
            if x + 1 in hashset:
                count += 1

        return count


print(Solution.countElements([1, 1, 3, 3, 5, 5, 7, 7]))
