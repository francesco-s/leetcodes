class Solution(object):
    def containsDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        return len(set(nums)) != len(nums)

# Test cases
solution = Solution()
print(solution.containsDuplicate([1, 2, 3, 4]))  # Expected: False
print(solution.containsDuplicate([1, 2, 3, 1]))  # Expected: True
print(solution.containsDuplicate([]))           # Expected: False
print(solution.containsDuplicate([1]))          # Expected: False
print(solution.containsDuplicate([1, 1, 1, 1])) # Expected: True
