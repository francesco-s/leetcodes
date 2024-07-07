# O(N^2)
from typing import List
import sys


class Solution:
    def maxSubArray(nums: List[int]):

        """
        Kadane solution
        :return:
        """

        max_sum = -9999999999
        curr_sum = 0

        for i in range(len(nums)):
            curr_sum += nums[i]

            if curr_sum > max_sum:
                max_sum = curr_sum

            if curr_sum < 0:
                curr_sum = 0

        return max_sum

    def maxSubArray3(nums: List[int]) -> int:
        def dp(i):
            if i >= len(nums): return 0
            if i not in memo:
                take = nums[i] + dp(i + 1)
                dontake = nums[i]
                memo[i] = max(take, dontake)
            return memo[i]

        memo = {}

        maxlen = dp(0)
        print(memo)

        return maxlen

    def maxSubArray2(nums: List[int]) -> int:
        def dp(i, csum):
            if i >= len(nums): return csum
            if (i, csum) not in memo:
                take = dp(i + 1, csum + nums[i])
                dontake = dp(i + 1, nums[i])
                memo[(i, csum)] = max(take, dontake, csum)
            return memo[(i, csum)]

        memo = {}

        def solve(i, curr_sum):
            nonlocal l
            if i >= len(nums): return
            take = dp(i + 1, curr_sum + nums[i])
            dontake = dp(i + 1, nums[i])
            if take > dontake:
                l.append(i)
                return solve(i + 1, curr_sum + nums[i])
            else:
                l = [i]
                return solve(i + 1, nums[i])

        memo = {}
        maxlen = dp(0, float('-inf'))

        l = []
        solve(0, float('-inf'))
        print(l)

        return maxlen


print(Solution.maxSubArray([-2, 1, -3, 4, -1, 2, 1, -5, 4]))
print(Solution.maxSubArray([5, 4, -1, 7, 8]))

print()
print(Solution.maxSubArray2([-2, 1, -3, 4, -1, 2, 1, -5, 4]))
print(Solution.maxSubArray2([5, 4, -1, 7, 8]))
