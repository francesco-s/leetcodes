from typing import List


class Solution:
    def longestOnes(nums: List[int], k: int) -> int:
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


print(Solution.longestOnes([1, 1, 1, 0, 0, 0, 1, 1, 1, 1, 0], k=1))
print(Solution.longestOnes([0, 0, 1, 1, 0, 0, 1, 1, 1, 0, 1, 1, 0, 0, 0, 1, 1, 1, 1], k=1))



