# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:

    def goodNodes(self, root: TreeNode) -> int:
        """
        Time Complexity (TC): O(N), where N is the number of nodes in the tree.
            - Each node is visited exactly once.
        Space Complexity (SC): O(H), where H is the height of the tree.
            - Due to recursion stack. In the worst case (skewed tree), H = N.
        """
        good_nodes = 0

        def dfs(node, max_so_far):
            if node is None:
                return

            nonlocal good_nodes

            if node.val >= max_so_far:
                good_nodes += 1

            curr_max = max(node.val, max_so_far)
            
            dfs(node.left, curr_max)
            dfs(node.right, curr_max)

        dfs(root, float('-inf'))
        return good_nodes

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
root1 = build_tree([3,1,4,3,None,1,5])
res1 = solution.goodNodes(root1)
print(f"Test case 1: {res1}")  # Expected: 4

# Test case 2 (example)
root2 = build_tree([3,3,None,4,2])
res2 = solution.goodNodes(root2)
print(f"Test case 2: {res2}")  # Expected: 3

# Test case 3 (single node)
root3 = build_tree([1])
res3 = solution.goodNodes(root3)
print(f"Test case 3: {res3}")  # Expected: 1

# Test case 4 (all increasing down right)
root4 = build_tree([1,None,2,None,3,None,4])
res4 = solution.goodNodes(root4)
print(f"Test case 4: {res4}")  # Expected: 4

# Test case 5 (all decreasing down left)
root5 = build_tree([5,4,None,3,None,2,None,1])
res5 = solution.goodNodes(root5)
print(f"Test case 5: {res5}")  # Expected: 1

# Test case 6 (mixed values with ties)
root6 = build_tree([2,2,2,1,2,2,3])
res6 = solution.goodNodes(root6)
print(f"Test case 6: {res6}")  # Expected: 6
