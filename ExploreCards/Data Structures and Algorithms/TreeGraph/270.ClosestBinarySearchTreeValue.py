import math
from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:

    def __init__(self):
        self.closest_diff = None
        self.closest = None

    def closestValue(self, root: Optional[TreeNode], target: float) -> int:
        self.closest = math.inf
        self.closest_diff = math.inf

        def dfs(root, target):

            if root is None:
                return

            if root.val < target:
                dfs(root.right, target)
            else:
                dfs(root.left, target)

            current_diff = abs(root.val - target)

            if current_diff < self.closest_diff or (current_diff == self.closest_diff and root.val < self.closest):
                self.closest = root.val
                self.closest_diff = current_diff
                
            return

        dfs(root, target)
        return self.closest


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

# values = [4, 2, 5, 1, 3]
# root = create_tree_from_list(values)
# print("Test case 0 - Expected: 4, Got:", solution.closestValue(root, target=3.714286))
# #
# values = [1]
# root = create_tree_from_list(values)
# print("Test case 1 - Expected: 1, Got:", solution.closestValue(root, target=4.428571))
#
# values = [1, None, 8]
# root = create_tree_from_list(values)
# print("Test case 2 - Expected: 1, Got:", solution.closestValue(root, target=3.0))
#
values = [4, 2, 5, 1, 3]
root = create_tree_from_list(values)
print("Test case 3 - Expected: 3, Got:", solution.closestValue(root, target=3.5))

values = [4, 2, 5, 1, 3]
root = create_tree_from_list(values)
print("Test case 4 - Expected: 4, Got:", solution.closestValue(root, target=4.5))

values = [1, None, 2]
root = create_tree_from_list(values)
print("Test case 4 - Expected: 2, Got:", solution.closestValue(root, target=3.428571))

values = [8, 1]
root = create_tree_from_list(values)
print("Test case 4 - Expected: 8, Got:", solution.closestValue(root, target=6))
