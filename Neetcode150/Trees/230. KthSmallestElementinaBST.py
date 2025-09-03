# Definition for a binary tree node.
from typing import List, Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:

    def kthSmallestInorder(self, root: Optional[TreeNode], k: int) -> int:
        def inorderTraversal(root) -> List[int]:
            if root is None:
                return []
        
            left = inorderTraversal(root.left)
            right = inorderTraversal(root.right)

            return left + [root.val] + right

        return inorderTraversal(root)[k -1]
    

    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        res = -1

        def inorderTraversal(root) -> List[int]:
            nonlocal k, res
            if root is None or k <= 0:
                return
            
            inorderTraversal(root.left)

            k -= 1
            if k == 0:
                res = root.val
                return

            inorderTraversal(root.right)

        inorderTraversal(root)
        return res
    
    
    def kthSmallestInorder(self, root: Optional[TreeNode], k: int) -> int:
        def inorderTraversal(root) -> List[int]:
            if root is None:
                return []
        
            left = inorderTraversal(root.left)
            right = inorderTraversal(root.right)

            return left + [root.val] + right

        return inorderTraversal(root)[k -1]

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
root1 = build_tree([3,1,4,None,2])
k1 = 1
res1 = solution.kthSmallest(root1, k1)
print(f"Test case 1: {res1}")  # Expected: 1

# Test case 3 (k = size)
root3 = build_tree([2,1,3])
k3 = 3
res3 = solution.kthSmallest(root3, k3)
print(f"Test case 3: {res3}")  # Expected: 3

# Test case 4 (single node)
root4 = build_tree([1])
k4 = 1
res4 = solution.kthSmallest(root4, k4)
print(f"Test case 4: {res4}")  # Expected: 1

# Test case 5 (right-skewed increasing)
root5 = build_tree([1,None,2,None,3,None,4])
k5 = 2
res5 = solution.kthSmallest(root5, k5)
print(f"Test case 5: {res5}")  # Expected: 2