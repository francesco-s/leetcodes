# Definition for a binary tree node.
from typing import List, Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        """
        Time Complexity: O(N), where N is the number of nodes in the tree.
            Each node is visited exactly once during the DFS traversal.
        Space Complexity: O(H), where H is the height of the tree.
            The space is used by the recursion stack and the levels list.
        """

        if root is None:
            return []

        levels = []

        def dfs(node, level):
            if node is None:
                return
                
            if len(levels) == level:
                levels.append(0)

            levels[level] = node.val # Overwrite until the most righ node
            
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

# Test case 1 (example)
root1 = build_tree([1,2,3,None,5,None,4])
res1 = solution.rightSideView(root1)
print(f"Test case 1: {res1}")  # Expected: [1,3,4]

# Test case 2 (right-leaning)
root2 = build_tree([1,None,3])
res2 = solution.rightSideView(root2)
print(f"Test case 2: {res2}")  # Expected: [1,3]

# Test case 3 (empty)
root3 = build_tree([])
res3 = solution.rightSideView(root3)
print(f"Test case 3: {res3}")  # Expected: []

# Test case 4 (left-heavy but with right nodes at deeper levels)
root4 = build_tree([1,2,3,4,None,None,5,None,None,None,6])
res4 = solution.rightSideView(root4)
print(f"Test case 4: {res4}")  # Expected: [1,3,5,6]

# Test case 5 (full tree)
root5 = build_tree([1,2,3,4,5,6,7])
res5 = solution.rightSideView(root5)
print(f"Test case 5: {res5}")  # Expected: [1,3,7]

# Test case 6 (gaps with None)
root6 = build_tree([1,2,3,None,5,None,7])
res6 = solution.rightSideView(root6)
print(f"Test case 6: {res6}")  # Expected: [1,3,7]
