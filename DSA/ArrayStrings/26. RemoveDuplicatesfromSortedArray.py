class Solution(object):
    def removeDuplicates(nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        size = len(nums)
        insertIndex = 1
        for i in range(1, size):
            if nums[i - 1] != nums[i]:
                nums[insertIndex] = nums[i]
                insertIndex = insertIndex + 1
        return insertIndex
            


# Example usage:
nums = [1, 1, 2]
# After calling removeDuplicates, nums should be modified to [1, 2, _]
# where _ represents irrelevant values beyond the new length.
print(Solution.removeDuplicates(nums))  # Output: 2

nums = [0,0,1,1,1,2,2,3,3,4]
print(Solution.removeDuplicates(nums))  # Output: 5