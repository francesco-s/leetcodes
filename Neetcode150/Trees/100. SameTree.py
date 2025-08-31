# Definition for a binary tree node.
from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:

    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        """
        Time Complexity (TC): O(N), where N is the number of nodes in the trees.
        Each node is visited once.
        Space Complexity (SC): O(H), where H is the height of the tree due to recursion stack.
        In worst case (skewed tree), H = N.
        """
        def check(p, q):
            if p is None and q is None:
                return True

            if p is None or q is None:  # If one is None (not both)
                return False

            if p.val != q.val:
                return False

            return check(p.left, q.left) and check(p.right, q.right)

        return check(p, q)

# Helpers: build tree from level order and serialize back for easy checking
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

def same_structure_values(root):
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
p1 = build_tree([1,2,3])
q1 = build_tree([1,2,3])
r1 = solution.isSameTree(p1, q1)
print(f"Test case 1: {r1}")  # Expected: True

# Test case 2
p2 = build_tree([1,2])
q2 = build_tree([1,None,2])
r2 = solution.isSameTree(p2, q2)
print(f"Test case 2: {r2}")  # Expected: False

# Test case 3
p3 = build_tree([1,2,1])
q3 = build_tree([1,1,2])
r3 = solution.isSameTree(p3, q3)
print(f"Test case 3: {r3}")  # Expected: False

# Test case 4
p4 = build_tree([])
q4 = build_tree([])
r4 = solution.isSameTree(p4, q4)
print(f"Test case 4: {r4}")  # Expected: True

# Test case 5
p5 = build_tree([1,None,2,3])
q5 = build_tree([1,None,2,3])
r5 = solution.isSameTree(p5, q5)
print(f"Test case 5: {r5}")  # Expected: True

# Test case 6
p6 = build_tree([1,2,3,4,5])
q6 = build_tree([1,2,3,4,None])
r6 = solution.isSameTree(p6, q6)
print(f"Test case 6: {r6}")  # Expected: False
