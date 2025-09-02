# Definition for a binary tree node.
from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:

    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        """
        Time Complexity: O(N), where N is the number of nodes in the tree.
        Space Complexity: O(H), where H is the height of the tree (due to recursion stack).
        """
        balanced = True

        def dfs(node):
            nonlocal balanced

            if node is None:
                return 0

            left = dfs(node.left)
            right = dfs(node.right)

            if abs(left - right) > 1:
                balanced = False

            return 1 + max(left, right)
        
        dfs(root)
        return balanced
    
    def isBalancedOptimized(self, root: Optional[TreeNode]) -> bool:
        """
        Optimized version: Returns False immediately when imbalance is detected.
        Time Complexity: O(N)
        Space Complexity: O(H)
        """
        def check(node):
            if not node:
                return 0
            left = check(node.left)
            if left == -1:
                return -1
            right = check(node.right)
            if right == -1:
                return -1
            if abs(left - right) > 1:
                return -1
            return 1 + max(left, right)
        return check(root) != -1

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
res1 = solution.isBalanced(root1)
print(f"Test case 1: {res1}")  # Expected: True

# Test case 2
root2 = build_tree([1,2,2,3,3,None,None,4,4])
res2 = solution.isBalanced(root2)
print(f"Test case 2: {res2}")  # Expected: False

# Test case 3
root3 = build_tree([])
res3 = solution.isBalanced(root3)
print(f"Test case 3: {res3}")  # Expected: True

# Test case 4 (skewed)
root4 = build_tree([1,2,None,3,None,4])
res4 = solution.isBalanced(root4)
print(f"Test case 4: {res4}")  # Expected: False

# Test case 5 (nearly balanced)
root5 = build_tree([1,2,3,4,None,None,None,5])
res5 = solution.isBalanced(root5)
print(f"Test case 5: {res5}")  # Expected: False

# Test case 6 (small balanced)
root6 = build_tree([1,2,2,3,None,None,3])
res6 = solution.isBalanced(root6)
print(f"Test case 6: {res6}")  # Expected: True
