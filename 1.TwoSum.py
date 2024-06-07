from typing import List


def twoSum(nums: List[int], target: int) -> List[int]:
    num_to_index = {}
    for i, value in enumerate(nums):
        complement = target - value
        if complement in num_to_index:
            return [num_to_index[complement], i]
        num_to_index[value] = i


def twoSum1(nums: List[int], target: int) -> List[int]:
    return next(([i, j] for i in range(len(nums)) for j in range(i + 1, len(nums)) if nums[i] + nums[j] == target),
                None)


def twoSum0(nums: List[int], target: int) -> List[int]:
    for i in range(0, len(nums)):
        for j in range(i + 1, len(nums)):
            if nums[i] + nums[j] == target:
                return [i, j]


print(twoSum([2, 7, 11, 15], 9))
print(twoSum([3, 2, 4], 6))
print(twoSum([3, 3], 6))
