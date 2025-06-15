# Example 1:
#
# Input: nums = [-3,2,-3,4,2]
# Output: 5
# Explanation: If you choose startValue = 4, in the third iteration your step by step sum is less than 1.
# step by step sum
# startValue = 4 | startValue = 5 | nums
#   (4 -3 ) = 1  | (5 -3 ) = 2    |  -3
#   (1 +2 ) = 3  | (2 +2 ) = 4    |   2
#   (3 -3 ) = 0  | (4 -3 ) = 1    |  -3
#   (0 +4 ) = 4  | (1 +4 ) = 5    |   4
#   (4 +2 ) = 6  | (5 +2 ) = 7    |   2

from typing import List


class Solution:
    def minStartValue(nums: List[int]) -> int:
        startValue = 1
        current_sum = 1

        for val in nums:
            if val >= 0:  # no worries when add a positive numbers
                current_sum += val
            else:
                if current_sum + val < 1:
                    startValue = startValue + abs(current_sum + val) + 1
                    current_sum = 1  # reset the sum
                else:
                    current_sum += val  # add a negative val but current_sum + val >= 1 -> no worries

        return startValue

    def minStartValue2(nums: List[int]) -> int:
        startValue, actual_value = 1, 1
        j = 0

        while True:
            actual_value = startValue
            while j < len(nums) and nums[j] + actual_value >= 1:
                actual_value = actual_value + nums[j]
                j += 1
            if j == len(nums):
                return startValue
            j = 0
            startValue += 1


print(Solution.minStartValue([-3, 2, -3, 4, 2]))
print(Solution.minStartValue2([-3, 2, -3, 4, 2]))
print()
print(Solution.minStartValue([1, 2]))
print(Solution.minStartValue2([1, 2]))
print()
print(Solution.minStartValue([1, -2, -3]))
print(Solution.minStartValue2([1, -2, -3]))
