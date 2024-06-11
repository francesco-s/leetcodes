from typing import List


# Example 1:
#
# Input: nums = [3,0,1] Output: 2 Explanation: n = 3 since there are 3 numbers, so all numbers are in the range [0,
# 3]. 2 is the missing number in the range since it does not appear in nums.
#
# Example 2:
#
# Input: nums = [0,1] Output: 2 Explanation: n = 2 since there are 2 numbers, so all numbers are in the range [0,
# 2]. 2 is the missing number in the range since it does not appear in nums.
#
# Example 3:
#
# Input: nums = [9,6,4,2,3,5,7,0,1] Output: 8 Explanation: n = 9 since there are 9 numbers, so all numbers are in the
# range [0,9]. 8 is the missing number in the range since it does not appear in nums.
#

class Solution:
    def missingNumber(nums: List[int]) -> int:
        expected_sum = len(nums) * (len(nums) + 1) // 2
        actual_sum = sum(nums)
        return expected_sum - actual_sum

    def missingNumber2(nums: List[int]) -> int:
        missing = len(nums)
        for i, num in enumerate(nums):
            missing ^= i ^ num
        return missing


print(Solution.missingNumber([9, 6, 4, 2, 3, 5, 7, 0, 1]))
print(Solution.missingNumber2([9, 6, 4, 2, 3, 5, 7, 0, 1]))
