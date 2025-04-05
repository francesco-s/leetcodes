from typing import List


class Solution:
    def longestOnes1(nums: List[int], k: int) -> int:
        left = 0
        max_length = 0
        zeros = 0

        for right in range(len(nums)):
            if nums[right] == 0:
                zeros += 1

            while zeros > k:
                if nums[left] == 0:
                    zeros -= 1
                left += 1

            max_length = max(max_length, right - left + 1)

        return max_length
    


    def longestOnes(nums: List[int], k = 1) -> int:
        max_cons_ones = 0
        right, left = 0 , 0
        zero_count = 0

        for right in range(0,len(nums)):
            if nums[right] == 0:
                zero_count += 1


            while zero_count > 1:
                if nums[left] == 0:
                    zero_count -= 1
                left += 1

            max_cons_ones = max(max_cons_ones, right - left + 1)
    

        return max_cons_ones



print(Solution.longestOnes([1, 1, 1, 0, 0, 0, 1, 1, 1, 1, 0], k=1))
print(Solution.longestOnes([1, 1, 1], k=1))
print(Solution.longestOnes([0], k=1))
print(Solution.longestOnes([0,0,1,1,0,0,1], k=1))

print(Solution.longestOnes([0, 0, 1, 1, 0, 0, 1, 1, 1, 0, 1, 1, 0, 0, 0, 1, 1, 1, 1], k=1))



