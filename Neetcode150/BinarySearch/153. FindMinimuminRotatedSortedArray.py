class Solution:

    def findMin(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        Time Complexity: O(log n)
        Space Complexity: O(1)
        """
        left, right = 0, len(nums) - 1

        while left < right:
            middle = left + ((right - left) // 2)
            if nums[middle] < nums[right]:
                right = middle
            else:
                left = middle + 1
        
        return nums[left]


# Test cases
solution = Solution()

# Test case 1
nums1 = [3,4,5,1,2]
result1 = solution.findMin(nums1)
print(f"Test case 1: {result1}")  # Expected: 1

# Test case 2
nums2 = [4,5,6,7,0,1,2]
result2 = solution.findMin(nums2)
print(f"Test case 2: {result2}")  # Expected: 0

# Test case 3
nums3 = [11,13,15,17]
result3 = solution.findMin(nums3)
print(f"Test case 3: {result3}")  # Expected: 11

# Test case 4
nums4 = [2,1]
result4 = solution.findMin(nums4)
print(f"Test case 4: {result4}")  # Expected: 1

# Test case 5
nums5 = [1]
result5 = solution.findMin(nums5)
print(f"Test case 5: {result5}")  # Expected: 1

# Test case 6
nums6 = [5,6,1,2,3,4]
result6 = solution.findMin(nums6)
print(f"Test case 6: {result6}")  # Expected: 1
