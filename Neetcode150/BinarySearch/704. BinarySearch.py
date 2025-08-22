from typing import List


class Solution:

    def search(self, nums: List[int], target: int) -> int:
        left, right = 0, len(nums) - 1

        while left <= right:
            middle = left + ((right - left) // 2)
            
            if nums[middle] == target:
                return middle
            elif nums[middle] > target:
                right = middle - 1
            else:
                left = middle + 1

        return -1

# Test cases
solution = Solution()

# Test case 1
nums1 = [-1,0,3,5,9,12]
target1 = 9
result1 = solution.search(nums1, target1)
print(f"Test case 1: {result1}")  # Expected: 4

# Test case 2
nums2 = [-1,0,3,5,9,12]
target2 = 2
result2 = solution.search(nums2, target2)
print(f"Test case 2: {result2}")  # Expected: -1

# Test case 3
nums3 = [5]
target3 = 5
result3 = solution.search(nums3, target3)
print(f"Test case 3: {result3}")  # Expected: 0

# Test case 4
nums4 = [1,2,3,4,5,6,7,8,9,10]
target4 = 1
result4 = solution.search(nums4, target4)
print(f"Test case 4: {result4}")  # Expected: 0

# Test case 5
nums5 = [1,2,3,4,5,6,7,8,9,10]
target5 = 10
result5 = solution.search(nums5, target5)
print(f"Test case 5: {result5}")  # Expected: 9

# Test case 6
nums6 = [1,3,5,7,9]
target6 = 7
result6 = solution.search(nums6, target6)
print(f"Test case 6: {result6}")  # Expected: 3
