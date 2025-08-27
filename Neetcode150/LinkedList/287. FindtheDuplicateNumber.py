class Solution:

    # Implements Floyd's Tortoise and Hare algorithm to find the duplicate number.
    # Time Complexity: O(n) - Each pointer traverses at most n steps.
    # Space Complexity: O(1) - Only constant extra space is used.
    def findDuplicate(self, nums: list[int]) -> int:
        slow = fast = nums[0]
        # Phase 1: Finding the intersection point in the cycle
        while True:
            slow = nums[slow]
            fast = nums[nums[fast]]
            if slow == fast:
                break
        # Phase 2: Finding the entrance to the cycle (duplicate number)
        slow = nums[0]
        while slow != fast:
            slow = nums[slow]
            fast = nums[fast]
        return slow

# Test cases
solution = Solution()

# Test case 1
nums1 = [1,3,4,2,2]
result1 = solution.findDuplicate(nums1)
print(f"Test case 1: {result1}")  # Expected: 2

# Test case 2
nums2 = [3,1,3,4,2]
result2 = solution.findDuplicate(nums2)
print(f"Test case 2: {result2}")  # Expected: 3

# Test case 3
nums3 = [1,1,2]
result3 = solution.findDuplicate(nums3)
print(f"Test case 3: {result3}")  # Expected: 1

# Test case 4
nums4 = [1,1]
result4 = solution.findDuplicate(nums4)
print(f"Test case 4: {result4}")  # Expected: 1

# Test case 5
nums5 = [2,2,2,2,2]
result5 = solution.findDuplicate(nums5)
print(f"Test case 5: {result5}")  # Expected: 2

# Test case 6
nums6 = [5,4,3,2,1,5]
result6 = solution.findDuplicate(nums6)
print(f"Test case 6: {result6}")  # Expected: 5
