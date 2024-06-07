from typing import List


# Input: nums = [-4,-1,0,3,10]
# Output: [0,1,9,16,100]
# Explanation: After squaring, the array becomes [16,1,0,9,100].
# After sorting, it becomes [0,1,9,16,100].

class Solution:
    def sortedSquares(nums: List[int]) -> List[int]:
        n = len(nums)
        # Find the index where non-negative numbers start

        non_neg_index = 0
        while non_neg_index < n and nums[non_neg_index] < 0:
            non_neg_index += 1

        # Use two pointers to merge squared negative numbers and squared positive numbers
        neg_ptr = non_neg_index - 1
        pos_ptr = non_neg_index
        result = []
        while neg_ptr >= 0 or pos_ptr < n:
            if neg_ptr >= 0 and (pos_ptr >= n or nums[neg_ptr] ** 2 < nums[pos_ptr] ** 2):
                result.append(nums[neg_ptr] ** 2)
                neg_ptr -= 1
            else:
                result.append(nums[pos_ptr] ** 2)
                pos_ptr += 1

        print(result)


Solution.sortedSquares([-4, -1, 0, 3, 10])
Solution.sortedSquares([-7, -3, 2, 3, 11])
Solution.sortedSquares([-4, -3, -2, -1, -1])
Solution.sortedSquares([1, 2, 3, 4, 11])
