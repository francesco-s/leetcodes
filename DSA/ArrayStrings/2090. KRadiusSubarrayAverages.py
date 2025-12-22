from typing import List


class Solution:
    def getAverages(nums: List[int], k: int) -> List[int]:
        if k > len(nums) // 2:
            return [-1] * len(nums)

        res = [-1] * k

        window_size = 2 * k + 1
        current_sum = 0

        if window_size <= len(nums):
            current_sum = sum(nums[0 : 2 * k + 1])
            res.append(current_sum // window_size)

        for i in range(k + 1, len(nums) - k):
            current_sum -= nums[i - k - 1]
            current_sum += nums[i + k]

            res.append(current_sum // window_size)

        res.extend([-1] * k)

        return res

    def getAverages2(nums: List[int], k: int) -> List[int]:
        if k > len(nums) // 2:
            return [-1] * len(nums)

        res = [-1] * k

        for i in range(k, len(nums) - k):
            res.append(sum(nums[i - k : i + k + 1]) // (2 * k + 1))

        res.extend([-1] * k)

        return res


print(Solution.getAverages([7, 4, 3, 9, 1, 8, 5, 2, 6], k=3))
print(Solution.getAverages([100000], k=0))
print(Solution.getAverages([8], k=100000))
print(Solution.getAverages([2, 1], k=1))
