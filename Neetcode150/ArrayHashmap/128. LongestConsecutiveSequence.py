from typing import List

# LeetCode 128: Longest Consecutive Sequence
# https://leetcode.com/problems/longest-consecutive-sequence/

class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        """
        Given an unsorted array of integers nums, return the length of the longest
        consecutive elements sequence.

        Constraints/Notes:
        - Must run in O(n) average time (hash set approach is typical).
        - Do not sort to meet the O(n) requirement.
        - Handle duplicates gracefully.

        Returns:
            int: Length of the longest consecutive sequence.
        """
        longest_consecutive = 0
        nums_set = set(nums)

        for num in nums_set:
            if num - 1 not in nums_set:
                current_num = num
                current_consecutive = 1

                while current_num + 1 in nums_set:
                    current_consecutive += 1
                    current_num += 1

                longest_consecutive = max(current_consecutive, longest_consecutive)
        
        return longest_consecutive


# Tests (no if __name__ == "__main__")
solution = Solution()

# Test case 1: basic example
nums1 = [100, 4, 200, 1, 3, 2]
res1 = solution.longestConsecutive(nums1)
print(f"Test case 1: {res1}")  # Expected: 4 (sequence: 1,2,3,4)

# Test case 2: with zeros and full run 0..8
nums2 = [0, 3, 7, 2, 5, 8, 4, 6, 0, 1]
res2 = solution.longestConsecutive(nums2)
print(f"Test case 2: {res2}")  # Expected: 9 (sequence: 0..8)

# Test case 3: empty array
nums3 = []
res3 = solution.longestConsecutive(nums3)
print(f"Test case 3: {res3}")  # Expected: 0

# Test case 4: single element
nums4 = [1]
res4 = solution.longestConsecutive(nums4)
print(f"Test case 4: {res4}")  # Expected: 1

# Test case 5: negatives and positives
nums5 = [9, 1, 4, 7, 3, -1, 0, 5, 8, -1, 6]
res5 = solution.longestConsecutive(nums5)
print(f"Test case 5: {res5}")  # Expected: 7 (sequence: 3..9)

# Test case 6: duplicates, ensure dedup and counting is correct
nums6 = [1, 2, 0, 1]
res6 = solution.longestConsecutive(nums6)
print(f"Test case 6: {res6}")  # Expected: 3 (sequence: 0,1,2)

# Test case 7: no consecutive sequences > 1
nums7 = [10, 30, 20]
res7 = solution.longestConsecutive(nums7)
print(f"Test case 7: {res7}")  # Expected: 1

# Test case 8: long run starting negative
nums8 = [-3, -2, -1, 0, 1, 2]
res8 = solution.longestConsecutive(nums8)
print(f"Test case 8: {res8}")  # Expected: 6
