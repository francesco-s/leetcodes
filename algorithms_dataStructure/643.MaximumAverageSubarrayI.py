from typing import List
import time


# Input: nums = [1,12,-5,-6,50,3], k = 4
# Output: 12.75000
# Explanation: Maximum average is (12 - 5 - 6 + 50) / 4 = 51 / 4 = 12.75

class Solution:
    def findMaxAverage2(nums: List[int], k: int) -> float:
        len_nums = len(nums)
        i = 0
        max_sum = 0
        while i <= len_nums - k + 1:
            current_window = nums[i:k + i]
            current_max_sum = sum(current_window)
            if max_sum < current_max_sum:
                max_sum = current_max_sum

            i += 1

        print(max_sum / k)

    def findMaxAverage(nums: List[int], k: int) -> float:
        len_nums = len(nums)
        max_sum = sum(nums[:k])
        window_sum = max_sum

        for i in range(1, len_nums - k + 1):
            window_sum = window_sum - nums[i - 1] + nums[i + k - 1]
            max_sum = max(max_sum, window_sum)

        print(max_sum / k)


Solution.findMaxAverage([1, 12, -5, -6, 50, 3], 4)

Solution.findMaxAverage2([1, 12, -5, -6, 50, 3], 4)
