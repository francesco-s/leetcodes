# Definition for a binary tree node.
from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:

    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        """
        Time Complexity (TC): O(N), where N is the number of nodes in the tree.
        Space Complexity (SC): O(N), for the output and recursion stack in the worst case.
        """
        if root is None:
            return []

        levels = []

        def dfs(node, level):
            if node is None:
                return
                
            if len(levels) == level:
                levels.append([])

            levels[level].append(node.val)

            dfs(node.left, level + 1)
            dfs(node.right, level + 1)
        
        dfs(root, 0)
        return levels

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
res1 = solution.levelOrder(root1)
print(f"Test case 1: {res1}")  # Expected: [[3],[9,20],[15,7]]

# Test case 2
root2 = build_tree([1])
res2 = solution.levelOrder(root2)
print(f"Test case 2: {res2}")  # Expected: [[1]]

# Test case 3
root3 = build_tree([])
res3 = solution.levelOrder(root3)
print(f"Test case 3: {res3}")  # Expected: []

# Test case 4 (skewed)
root4 = build_tree([1,2,None,3,None,4])
res4 = solution.levelOrder(root4)
print(f"Test case 4: {res4}")  # Expected: [[1],[2],[3],[4]]

# Test case 5 (full tree)
root5 = build_tree([1,2,3,4,5,6,7])
res5 = solution.levelOrder(root5)
print(f"Test case 5: {res5}")  # Expected: [[1],[2,3],[4,5,6,7]]

# Test case 6 (with Nones inside)
root6 = build_tree([1,2,3,None,5,None,7])
res6 = solution.levelOrder(root6)
print(f"Test case 6: {res6}")  # Expected: [[1],[2,3],[5,7]]
