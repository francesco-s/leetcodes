# Example 1:
#
# Input: nums = [5,7,3,9,4,9,8,3,1] Output: 8 Explanation: The maximum integer in the array is 9 but it is repeated.
# The number 8 occurs only once, so it is the answer.
#
# Example 2:
#
# Input: nums = [9,9,8,8]
# Output: -1
# Explanation: There is no number that occurs only once.
from collections import defaultdict
from typing import List


class Solution:

    def largestUniqueNumber(nums: List[int]) -> int:
        num_count = defaultdict(int)
        max_unique = -1

        for num in nums:
            num_count[num] += 1

        for key, value in num_count.items():
            if value == 1:
                max_unique = max(max_unique, key)

        return max_unique

    def largestUniqueNumber2(nums: List[int]) -> int:
        num_count = defaultdict(int)
        duplicates = set()

        for num in nums:
            if num not in duplicates:
                num_count[num] += 1
            if num_count[num] == 2:
                duplicates.add(num)

        [num_count.pop(list(duplicates)[i]) for i in range(len(duplicates))]

        if len(num_count) > 0:
            return max(num_count)
        else:
            return -1


print(Solution.largestUniqueNumber([5, 7, 3, 9, 4, 9, 8, 3, 1, 3]))
