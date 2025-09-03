# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:

    def buildTree(self, preorder, inorder):
        """
        :type preorder: List[int]
        :type inorder: List[int]
        :rtype: TreeNode
        """
        if not preorder or not inorder:
            return None

        root = TreeNode(preorder[0])
        left = inorder.index(preorder[0])

        root.left = self.buildTree(preorder[1:1 + left], inorder[:left])
        root.right = self.buildTree(preorder[1 + left:], inorder[left + 1:])
        return root

# Helpers: serialize tree to level-order for validation
from collections import deque

def tree_to_level(root):
    if not root:
        return []
    out, q = [], deque([root])
    while q:
        node = q.popleft()
        if node:
            out.append(node.val)
            q.append(node.left)
            q.append(node.right)
        else:
            out.append(None)
    while out and out[-1] is None:
        out.pop()
    return out

# Test cases
solution = Solution()

# Test case 1 (example)
pre1 = [3,9,20,15,7]
in1  = [9,3,15,20,7]
root1 = solution.buildTree(pre1, in1)
print(f"Test case 1: {tree_to_level(root1)}")  # Expected: [3, 9, 20, None, None, 15, 7]

# Test case 2 (single node)
pre2 = [-1]
in2  = [-1]
root2 = solution.buildTree(pre2, in2)
print(f"Test case 2: {tree_to_level(root2)}")  # Expected: [-1]

# Test case 3 (left-skewed)
pre3 = [3,2,1]
in3  = [1,2,3]
root3 = solution.buildTree(pre3, in3)
print(f"Test case 3: {tree_to_level(root3)}")  # Expected: [3, 2, None, 1]

# Test case 4 (right-skewed)
pre4 = [1,2,3]
in4  = [1,2,3]
root4 = solution.buildTree(pre4, in4)
print(f"Test case 4: {tree_to_level(root4)}")  # Expected: [1, None, 2, None, 3]

# Test case 5 (balanced)
pre5 = [1,2,4,5,3,6,7]
in5  = [4,2,5,1,6,3,7]
root5 = solution.buildTree(pre5, in5)
print(f"Test case 5: {tree_to_level(root5)}")  # Expected: [1,2,3,4,5,6,7]

# Test case 6 (another mixed)
pre6 = [6,2,1,4,3,5,8,7,9]
in6  = [1,2,3,4,5,6,7,8,9]
root6 = solution.buildTree(pre6, in6)
print(f"Test case 6: {tree_to_level(root6)}")  # Expected: [6,2,8,1,4,7,9, None, None, 3,5]
