# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def maxDepth(self, root: TreeNode) -> int:
        # Placeholder for the solution
        def dfs(root):
            if not root:
                return 0
            left_height = 1 + self.maxDepth(root.left)
            right_height = 1 + self.maxDepth(root.right)
            
            return max(left_height, right_height)

        return dfs(root)

# Test cases
solution = Solution()

# Test case 1
root1 = TreeNode(3)
root1.left = TreeNode(9)
root1.right = TreeNode(20, TreeNode(15), TreeNode(7))
result1 = solution.maxDepth(root1)
print(f"Test case 1: {result1}")  # Expected: 3

# Test case 2
root2 = TreeNode(1, None, TreeNode(2))
result2 = solution.maxDepth(root2)
print(f"Test case 2: {result2}")  # Expected: 2

# Test case 3
root3 = None
result3 = solution.maxDepth(root3)
print(f"Test case 3: {result3}")  # Expected: 0

# Test case 4
root4 = TreeNode(0)
result4 = solution.maxDepth(root4)
print(f"Test case 4: {result4}")  # Expected: 1