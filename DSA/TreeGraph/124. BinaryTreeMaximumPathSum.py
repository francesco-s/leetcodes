# Definition for a binary tree node.
import math
from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        self.max_sum = -math.inf

        def dfs(root):
            if root is None:
                return 0

            left_max = dfs(root.left)
            right_max = dfs(root.right)

            self.max_sum = max(root.val, self.max_sum, root.val + left_max + right_max, root.val + left_max, root.val + right_max)

            return max(root.val, root.val + left_max, root.val + right_max)

        dfs(root)
        return self.max_sum


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

# root = None
# print("Test case 1 - Expected: 0, Got:", solution.maxPathSum(root))
#
# root = TreeNode(1)
# print("Test case 2 - Expected: 1, Got:", solution.maxPathSum(root))

values = [1, 2, 3]
root = create_tree_from_list(values)
print("Test case 1 - Expected: 6, Got:", solution.maxPathSum(root))

values = [-10, 9, 20, None, None, 15, 7]
root = create_tree_from_list(values)
print("Test case 2 - Expected: 42, Got:", solution.maxPathSum(root))

values = [-3]
root = create_tree_from_list(values)
print("Test case 3 - Expected: -3, Got:", solution.maxPathSum(root))

values = [2, -1]
root = create_tree_from_list(values)
print("Test case 4 - Expected: 2, Got:", solution.maxPathSum(root))
