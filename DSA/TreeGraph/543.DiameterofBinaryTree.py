from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:

    def __init__(self):
        self.max_len = None

    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        self.max_len = 0

        def dfs(root):
            if root is None:
                return 0

            len_right = dfs(root.right)
            len_left = dfs(root.left)

            self.max_len = max(self.max_len, len_left + len_right)
            return max(len_left, len_right) + 1

        dfs(root)
        return self.max_len


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

values = [1, 2, 3, 4, 5]
root = create_tree_from_list(values)
print("Test case 0 - Expected: 3, Got:", solution.diameterOfBinaryTree(root))

values = [1, 2]
root = create_tree_from_list(values)
print("Test case 0 - Expected: 1, Got:", solution.diameterOfBinaryTree(root))

# root = None
# print("Test case 1 - Expected: 0, Got:", solution.maxAncestorDiff(root))
#
# root = TreeNode(1)
# print("Test case 2 - Expected: 1, Got:", solution.maxAncestorDiff(root))
#
# values = [1, 2, 3, 4, 5, None, None]
# root = create_tree_from_list(values)
# print("Test case 3 - Expected: 2, Got:", solution.maxAncestorDiff(root))
#
# values = [1, 2, None, 3, None, 4, None]
# root = create_tree_from_list(values)
# print("Test case 4 - Expected: 4, Got:", solution.maxAncestorDiff(root))
#
# values = [1, None, 2, None, 3, None, 4]
# root = create_tree_from_list(values)
# print("Test case 5 - Expected: 4, Got:", solution.maxAncestorDiff(root))
#
# values = [1, 2, 3, 4, None, None, 5]
# root = create_tree_from_list(values)
# print("Test case 6 - Expected: 3, Got:", solution.maxAncestorDiff(root))
