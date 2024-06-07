# Example 1:
#
# Input: nums = [1,2,3,4]
# Output: [1,3,6,10]
# Explanation: Running sum is obtained as follows: [1, 1+2, 1+2+3, 1+2+3+4].
#
# Example 2:
#
# Input: nums = [1,1,1,1,1]
# Output: [1,2,3,4,5]
# Explanation: Running sum is obtained as follows: [1, 1+1, 1+1+1, 1+1+1+1, 1+1+1+1+1].
#
# Example 3:
#
# Input: nums = [3,1,2,10,1]
# Output: [3,4,6,16,17]
from typing import List

class Solution:
    def runningSum(nums: List[int]) -> List[int]:
        for i in range(1, len(nums)):
            nums[i] += nums[i - 1]
        return nums


print(Solution.runningSum([1, 2, 3, 4]))
print(Solution.runningSum([1, 1, 1, 1, 1]))
print(Solution.runningSum([3, 1, 2, 10, 1]))
