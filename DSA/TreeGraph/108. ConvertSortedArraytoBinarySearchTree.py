class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def sortedArrayToBST(self, nums):
        # Placeholder for the actual implementation
        def helper(left, right):
            if left > right:
                return None
            
            middle = (left + right) // 2
            root = TreeNode(nums[middle], helper(left, middle - 1), helper(middle + 1, right))
            return root


        return helper(0, len(nums) - 1)

# Test cases
solution = Solution()

# Test case 1
nums1 = [-10, -3, 0, 5, 9]  
result1 = solution.sortedArrayToBST(nums1)
print(f"Test case 1: {result1}")  # Expected: A balanced BST with root 0 -> [0,-3,9,-10,null,5]

# Test case 2
nums2 = [1, 3]
result2 = solution.sortedArrayToBST(nums2)
print(f"Test case 2: {result2}")  # Expected: A balanced BST with root 3 or 1

# Test case 3
nums3 = []
result3 = solution.sortedArrayToBST(nums3)
print(f"Test case 3: {result3}")  # Expected: None