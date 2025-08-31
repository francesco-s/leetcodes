# Definition for a binary tree node.
from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:

    def maxDepth(self, root: Optional[TreeNode]) -> int:
        """
        Time Complexity (TC): O(n), where n is the number of nodes in the tree.
        Each node is visited once.

        Space Complexity (SC): O(h), where h is the height of the tree.
        This is due to the recursion stack. In the worst case (skewed tree), h = n.
        """
        if root is None:
            return 0
        
        return 1 + max(self.maxDepth(root.left), self.maxDepth(root.right))

# Helpers: build a tree from level-order list and serialize back
from collections import deque

def build_tree(level):
    if not level:
        return None
    it = iter(level)
    root_val = next(it)
    if root_val is None:
        return None
    root = TreeNode(root_val)
    q = deque([root])
    for a, b in zip(it, it):
        node = q.popleft()
        if a is not None:
            node.left = TreeNode(a)
            q.append(node.left)
        if b is not None:
            node.right = TreeNode(b)
            q.append(node.right)
    return root

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

# Test case 1
root1 = build_tree([3,9,20,None,None,15,7])
res1 = solution.maxDepth(root1)
print(f"Test case 1: {res1}")  # Expected: 3

# Test case 2
root2 = build_tree([1,None,2])
res2 = solution.maxDepth(root2)
print(f"Test case 2: {res2}")  # Expected: 2

# Test case 3
root3 = build_tree([])
res3 = solution.maxDepth(root3)
print(f"Test case 3: {res3}")  # Expected: 0

# Test case 4
root4 = build_tree([1,2,3,4,5])
res4 = solution.maxDepth(root4)
print(f"Test case 4: {res4}")  # Expected: 3

# Test case 5
root5 = build_tree([1])
res5 = solution.maxDepth(root5)
print(f"Test case 5: {res5}")  # Expected: 1

# Test case 6
root6 = build_tree([1,2,None,3,None,4])
res6 = solution.maxDepth(root6)
print(f"Test case 6: {res6}")  # Expected: 4
