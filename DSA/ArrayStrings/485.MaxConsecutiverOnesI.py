from typing import List


class Solution:
    def longestOnes1(nums: List[int]) -> int:
        len_nums = len(nums)
        i = 0
        nums_ones, nums_zeros_before, nums_zeros_after, max_consecutive_onesIII = 0, 0, 0, 0

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

            max_consecutive_onesIII = max(max_consecutive_onesIII, nums_ones)

        return max_consecutive_onesIII
    


    
    def longestOnes(nums: List[int]) -> int:
        max_cons_ones = 0
        global_max = 0
        for num in nums:
            if num == 1:
                max_cons_ones += 1
                if max_cons_ones > global_max:
                    global_max = max_cons_ones
            if num == 0:
                max_cons_ones = 0
        return global_max


print(Solution.longestOnes([1, 1, 1, 0, 0, 0, 1, 1, 1, 1, 0]))
print(Solution.longestOnes([0, 0, 1, 1, 0, 0, 1, 1, 1, 0, 1, 1, 0, 0, 0, 1, 1, 1, 1]))