from collections import defaultdict
from typing import List


# Example 1:
#
# Input: nums = [0,1]
# Output: 2
# Explanation: [0, 1] is the longest contiguous subarray with an equal number of 0 and 1.
#
# Example 2:
#
# Input: nums = [0,1,0]
# Output: 2
# Explanation: [0, 1] (or [1, 0]) is a longest contiguous subarray with equal number of 0 and 1.

# [0, 1, 1, 1, 1, 1, 0, 1, 0, 1]
# [1, 1, 0, 0, 1, 1, 0, 1, 0, 1]
# [0, 0, 0, 1, 1, 0, 0, 1, 1, 0]
# [1, 0, 1, 1, 0, 1, 1, 1, 0, 1]
# [0, 0, 0, 1, 1, 0, 1, 1, 1, 1]
# [1, 0, 0, 0, 1, 1, 0, 1, 1, 0]
# [0, 0, 1, 0, 0, 1, 1, 1, 0, 1]
# [0, 1, 0, 1, 0, 0, 1, 0, 0, 0]
# [1, 1, 1, 1, 1, 1, 1, 1]


class Solution:

    def findMaxLength(nums: List[int]) -> int:
        count_dict = {0: -1}  # To handle the case when the subarray starts from index 0

        cumulative_count, max_len = 0, 0

        for i in range(len(nums)):
            if nums[i] == 1:
                cumulative_count += 1
            else:
                cumulative_count -= 1

            if cumulative_count in count_dict:
                max_len = max(max_len, i - count_dict[cumulative_count])
            else:
                count_dict[cumulative_count] = i

        return max_len

    def findMaxLength2(nums: List[int]) -> int:
        count_dict = defaultdict(list)

        i, cumulative_count, max_len = 0, 0, 0
        count_dict[0] = [0]  # To handle the case when the subarray starts from index 0

        while i < len(nums):
            if nums[i] == 1:
                cumulative_count += 1
            else:
                cumulative_count -= 1

            if len(count_dict[cumulative_count]) <= 1:
                count_dict[cumulative_count].append(i + 1)
            else:
                count_dict[cumulative_count][1] = i + 1

            max_len = max(max_len, count_dict[cumulative_count][-1] - count_dict[cumulative_count][0])
            i += 1

        return max_len


print(Solution.findMaxLength([0, 1]))
print(Solution.findMaxLength([0, 1, 0]))
print(Solution.findMaxLength([0, 1, 1, 1, 1, 1, 0, 1, 0, 1]))
print(Solution.findMaxLength([0, 1, 0, 1, 0, 0, 1, 0, 0, 0]))
print(Solution.findMaxLength([1, 1, 1, 1, 1, 1, 1, 1]))
