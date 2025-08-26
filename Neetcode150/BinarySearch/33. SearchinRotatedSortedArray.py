from typing import List


class Solution:

    def search(self, nums: List[int], target: int) -> int:
        """
        Searches for a target value in a rotated sorted array.

        Time Complexity: O(log n)
            - Finding the rotation index: O(log n)
            - Binary search in one of the two sorted subarrays: O(log n)
        Space Complexity: O(1)
            - Only a constant amount of extra space is used.
        """
        left, right = 0, len(nums) - 1
        n = len(nums)

        # Find the index of the smallest value using binary search.
        while left < right:
            middle = left + ((right - left) // 2)
            if nums[middle] < nums[right]:
                right = middle
            else:
                left = middle + 1

        def binarySearch(left_boundary, right_boundary, target):
            left, right = left_boundary, right_boundary
            while left <= right:
                middle = left + ((right - left) // 2)
                if nums[middle] == target:
                    return middle
                elif nums[middle] > target:
                    right = middle - 1
                else:
                    left = middle + 1
            return -1

        if (answer := binarySearch(0, left - 1, target)) != -1:
            return answer

        return binarySearch(left, n - 1, target)

# Test cases
solution = Solution()

# Test case 1
nums1 = [4,5,6,7,0,1,2]
target1 = 0
result1 = solution.search(nums1, target1)
print(f"Test case 1: {result1}")  # Expected: 4

# Test case 2
nums2 = [4,5,6,7,0,1,2]
target2 = 3
result2 = solution.search(nums2, target2)
print(f"Test case 2: {result2}")  # Expected: -1

# Test case 3
nums3 = [1]
target3 = 0
result3 = solution.search(nums3, target3)
print(f"Test case 3: {result3}")  # Expected: -1

# Test case 4
nums4 = [1]
target4 = 1
result4 = solution.search(nums4, target4)
print(f"Test case 4: {result4}")  # Expected: 0

# Test case 5
nums5 = [3,4,5,6,1,2]
target5 = 1
result5 = solution.search(nums5, target5)
print(f"Test case 5: {result5}")  # Expected: 4

# Test case 6
nums6 = [5,1,3]
target6 = 3
result6 = solution.search(nums6, target6)
print(f"Test case 6: {result6}")  # Expected: 2
