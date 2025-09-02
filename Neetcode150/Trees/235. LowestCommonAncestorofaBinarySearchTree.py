# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:

    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        """
        Time Complexity: O(h), where h is the height of the tree.
        Space Complexity: O(h), due to recursion stack. For a balanced BST, h = log n; for a skewed tree, h = n.
        """
        if not root or not p or not q:
            return None

        curr_val = root.val
        p_val = p.val
        q_val = q.val

        if p_val > curr_val and q_val > curr_val:
            return self.lowestCommonAncestor(root.right, p, q)
        if p_val < curr_val and q_val < curr_val:
            return self.lowestCommonAncestor(root.left, p, q)
        else:
            return root

# Helpers: build a BST from level-order list, find node by value, and serialize node
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

def find_node(root, val):
    # Since it's a BST, use BST property to locate the node by value
    cur = root
    while cur:
        if val == cur.val:
            return cur
        cur = cur.left if val < cur.val else cur.right
    return None

def node_val(node):
    return node.val if node else None

# Test cases
solution = Solution()

# Test case 1 (classic example)
root1 = build_tree([6,2,8,1,4,7,9,None,None,3,5])
p1 = find_node(root1, 2)
q1 = find_node(root1, 8)
res1 = solution.lowestCommonAncestor(root1, p1, q1)
print(f"Test case 1: {node_val(res1)}")  # Expected: 6

# Test case 2 (LCA is one of the nodes)
p2 = find_node(root1, 2)
q2 = find_node(root1, 4)
res2 = solution.lowestCommonAncestor(root1, p2, q2)
print(f"Test case 2: {node_val(res2)}")  # Expected: 2

# Test case 3 (both on right subtree)
p3 = find_node(root1, 7)
q3 = find_node(root1, 9)
res3 = solution.lowestCommonAncestor(root1, p3, q3)
print(f"Test case 3: {node_val(res3)}")  # Expected: 8

# Test case 4 (both on left subtree, deeper split)
p4 = find_node(root1, 3)
q4 = find_node(root1, 5)
res4 = solution.lowestCommonAncestor(root1, p4, q4)
print(f"Test case 4: {node_val(res4)}")  # Expected: 4

# Test case 5 (single node tree)
root5 = build_tree([1])
p5 = find_node(root5, 1)
q5 = find_node(root5, 1)
res5 = solution.lowestCommonAncestor(root5, p5, q5)
print(f"Test case 5: {node_val(res5)}")  # Expected: 1

# Test case 6 (skewed BST)
root6 = build_tree([5,3,None,2,None,1])  # left-skewed representation
p6 = find_node(root6, 2)
q6 = find_node(root6, 1)
res6 = solution.lowestCommonAncestor(root6, p6, q6)
print(f"Test case 6: {node_val(res6)}")  # Expected: 2
