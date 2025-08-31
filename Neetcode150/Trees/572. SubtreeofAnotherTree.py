# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:

    # Time Complexity: O(m * n) in worst case, where m = #nodes in root, n = #nodes in subRoot.
    # For each node in root, we may compare up to n nodes in subRoot.
    # Space Complexity: O(max(m, n)) due to recursion stack in worst case (skewed trees).
    def isSubtree(self, root, subRoot):
        if root is None:
            # If subRoot is also None, it's a subtree; otherwise, False.
            return subRoot is None

        def sameTree(p, q):
            if p is None and q is None:
                return True
            if p is None or q is None:
                return False
            if p.val != q.val:
                return False
            return sameTree(p.left, q.left) and sameTree(p.right, q.right)

        if sameTree(root, subRoot):
            return True

        return self.isSubtree(root.left, subRoot) or self.isSubtree(root.right, subRoot)

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
root1 = build_tree([3,4,5,1,2])
sub1  = build_tree([4,1,2])
res1 = solution.isSubtree(root1, sub1)
print(f"Test case 1: {res1}")  # Expected: True

# Test case 2
root2 = build_tree([3,4,5,1,2,None,None,None,None,0])
sub2  = build_tree([4,1,2])
res2 = solution.isSubtree(root2, sub2)
print(f"Test case 2: {res2}")  # Expected: False

# Test case 3 (identical trees)
root3 = build_tree([1,1])
sub3  = build_tree([1,1])
res3 = solution.isSubtree(root3, sub3)
print(f"Test case 3: {res3}")  # Expected: True

# Test case 4 (subRoot is None)
root4 = build_tree([1,2,3])
sub4  = build_tree([])
res4 = solution.isSubtree(root4, sub4)
print(f"Test case 4: {res4}")  # Expected: True

# Test case 5 (root is None, subRoot not None)
root5 = build_tree([])
sub5  = build_tree([1])
res5 = solution.isSubtree(root5, sub5)
print(f"Test case 5: {res5}")  # Expected: False

# Test case 6 (deep subtree)
root6 = build_tree([1,2,3,4,5,None,None,6])
sub6  = build_tree([2,4,5,6])
res6 = solution.isSubtree(root6, sub6)
print(f"Test case 6: {res6}")  # Expected: True
