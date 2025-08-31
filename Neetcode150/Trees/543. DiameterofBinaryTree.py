# Definition for a binary tree node.
from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:

    # Time Complexity: O(N), where N is the number of nodes in the tree.
    # Each node is visited once during DFS traversal.
    # Space Complexity: O(H), where H is the height of the tree.
    # The recursion stack can go up to the height of the tree.

    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        diameter = 0

        def dfs(root):
            if root is None:
                return -1

            nonlocal diameter

            left_path = dfs(root.left)
            right_path = dfs(root.right)

            diameter = max(diameter, left_path + right_path + 2)
        
            return 1 + max(left_path, right_path)
        dfs(root)
        return diameter

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
root1 = build_tree([1,2,3,4,5])
res1 = solution.diameterOfBinaryTree(root1)
print(f"Test case 1: {res1}")  # Expected: 3

# Test case 2
root2 = build_tree([1,2])
res2 = solution.diameterOfBinaryTree(root2)
print(f"Test case 2: {res2}")  # Expected: 1

# Test case 3
root3 = build_tree([1])
res3 = solution.diameterOfBinaryTree(root3)
print(f"Test case 3: {res3}")  # Expected: 0

# Test case 4 (skewed chain)
root4 = build_tree([1,2,None,3,None,4,None])
res4 = solution.diameterOfBinaryTree(root4)
print(f"Test case 4: {res4}")  # Expected: 3

# Test case 5 (balanced)
root5 = build_tree([4,2,7,1,3,6,9])
res5 = solution.diameterOfBinaryTree(root5)
print(f"Test case 5: {res5}")  # Expected: 4

# Test case 6 (empty)
root6 = build_tree([])
res6 = solution.diameterOfBinaryTree(root6)
print(f"Test case 6: {res6}")  # Expected: 0
