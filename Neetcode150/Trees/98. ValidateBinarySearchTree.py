# Definition for a binary tree node.
from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:

    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        
        def dfs(node, left, right):
            if node is None:
                return True

            if not(left < node.val < right):
                return False

            return dfs(node.left, left, node.val) and dfs(node.right, node.val, right)


        return dfs(root, float("-inf"), float("inf"))

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

# Test case 1 (valid)
root1 = build_tree([2,1,3])
res1 = solution.isValidBST(root1)
print(f"Test case 1: {res1}")  # Expected: True

# Test case 2 (invalid: 4 under right of 5)
root2 = build_tree([5,1,4,None,None,3,6])
res2 = solution.isValidBST(root2)
print(f"Test case 2: {res2}")  # Expected: False

# Test case 3 (invalid deeper: 3 in right subtree of 5)
root3 = build_tree([5,4,6,None,None,3,7])
res3 = solution.isValidBST(root3)
print(f"Test case 3: {res3}")  # Expected: False

# Test case 4 (single node)
root4 = build_tree([1])
res4 = solution.isValidBST(root4)
print(f"Test case 4: {res4}")  # Expected: True

# Test case 5 (duplicates should fail for strict BST)
root5 = build_tree([2,2,2])
res5 = solution.isValidBST(root5)
print(f"Test case 5: {res5}")  # Expected: False

# Test case 6 (large valid)
root6 = build_tree([10,5,15,3,7,12,18,1,4,6,9,11,13,16,20])
res6 = solution.isValidBST(root6)
print(f"Test case 6: {res6}")  # Expected: True
