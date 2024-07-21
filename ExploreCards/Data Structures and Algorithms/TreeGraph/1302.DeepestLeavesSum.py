# Definition for a binary tree node.
from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def __init__(self):
        self.prova = None
        self.max_depth = None
        self.current_depth = None
        self.current_sum = None

    def deepestLeavesSum(self, root: Optional[TreeNode]) -> int:

        self.current_sum = 0
        self.current_depth = 0

        def max_depth(root):
            if root is None:
                return 0
            left = max_depth(root.left)
            right = max_depth(root.right)

            return 1 + max(left, right)

        self.max_depth = max_depth(root)

        def dfs(root, current_depth):
            if root is None:
                return 0

            dfs(root.left, 1 + current_depth)
            dfs(root.right, 1 + current_depth)

            if root.left is None and root.right is None and current_depth == self.max_depth:
                self.current_sum += root.val

            return

        dfs(root, 1)

        return self.current_sum


def create_tree_from_list(values):
    """
    Create a binary tree from a list of values (breadth-first order).
    `None` values in the list represent null nodes.
    """
    if not values:
        return None

    root = TreeNode(values[0])
    queue = [root]
    i = 1

    while queue and i < len(values):
        node = queue.pop(0)

        if values[i] is not None:
            node.left = TreeNode(values[i])
            queue.append(node.left)
        i += 1

        if i < len(values) and values[i] is not None:
            node.right = TreeNode(values[i])
            queue.append(node.right)
        i += 1

    return root


def create_list_from_tree(root):
    """
    Create a list from a binary tree (breadth-first order).
    `None` values in the list represent null nodes.
    """
    if not root:
        return []

    result = []
    queue = [root]

    while queue:
        node = queue.pop(0)
        if node:
            result.append(node.val)
            queue.append(node.left)
            queue.append(node.right)
        else:
            result.append(None)

    # Remove trailing None values to represent the actual structure of the tree
    while result and result[-1] is None:
        result.pop()

    return result


solution = Solution()

values = [1, 2, 3, 4, 5, None, 6, 7, None, None, None, None, 8]
root = create_tree_from_list(values)
print("Test case 3 - Expected: 15, Got:", solution.deepestLeavesSum(root))
