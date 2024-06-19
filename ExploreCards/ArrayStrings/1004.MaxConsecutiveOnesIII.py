from typing import List


# Input: nums = [1,1,1,0,0,0,1,1,1,1,0], k = 2
# Output: 6
# Explanation: [1,1,1,0,0,1,1,1,1,1,1]
# Bolded numbers were flipped from 0 to 1. The longest subarray is underlined.


# Input: nums = [0,0,1,1,0,0,1,1,1,0,1,1,0,0,0,1,1,1,1], k = 3
# Output: 10
# Explanation: [0,0,1,1,1,1,1,1,1,1,1,1,0,0,0,1,1,1,1]
# Bolded numbers were flipped from 0 to 1. The longest subarray is underlined.


class Solution:
    def longestOnes(nums: List[int], k: int) -> int:
        len_nums = len(nums)
        i = 0
        nums_zeros_before = 0
        nums_zeros_after = 0
        max_consecutive_onesIII = 0

        while i < len_nums:
            nums_ones = 0
            nums_zeros_before = nums_zeros_after
            nums_zeros_after = 0

            while i < len_nums and nums[i] == 0:
                nums_zeros_before += 1
                i += 1
            while i < len_nums and nums[i] == 1:
                nums_ones += 1
                i += 1
            while i < len_nums and nums[i] == 0:
                nums_zeros_after += 1
                i += 1

            # print('zeros before: ', nums_zeros_before)
            # print('ones: ', nums_ones)
            # print('zeros after: ', nums_zeros_after)

            sum_zeros_before_after = nums_zeros_before + nums_zeros_after

            if sum_zeros_before_after > k:
                max_consecutive_onesIII = max(max_consecutive_onesIII, nums_ones + k)
            else:
                max_consecutive_onesIII = max(max_consecutive_onesIII, nums_ones + sum_zeros_before_after)

        return max_consecutive_onesIII


print(Solution.longestOnes([1, 1, 1, 0, 0, 0, 1, 1, 1, 1, 0], k=2))
print(Solution.longestOnes([0, 0, 1, 1, 0, 0, 1, 1, 1, 0, 1, 1, 0, 0, 0, 1, 1, 1, 1], k=3))
