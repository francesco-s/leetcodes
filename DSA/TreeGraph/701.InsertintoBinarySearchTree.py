from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:

    def __init__(self):
        self.max_len = None

    def insertIntoBST(self, root: Optional[TreeNode], val: int) -> Optional[TreeNode]:

        if root is None:
            return TreeNode(val)

        if root.val < val:
            root.right = self.insertIntoBST(root.right, val)
        else:
            root.left = self.insertIntoBST(root.left, val)

        return root


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

values = [4, 2, 7, 1, 3]
root = create_tree_from_list(values)
print("Test case 0 - Expected: [4,2,7,1,3,5], Got:", create_list_from_tree(solution.insertIntoBST(root, val=5)))

values = [40, 20, 60, 10, 30, 50, 70]
root = create_tree_from_list(values)
print("Test case 1 - Expected: [40,20,60,10,30,50,70,null,null,25], Got:",
      create_list_from_tree(solution.insertIntoBST(root, val=25)))

values = [4, 2, 7, 1, 3, None, None, None, None, None, None]
root = create_tree_from_list(values)
print("Test case 2 - Expected: [4,2,7,1,3,5], Got:", create_list_from_tree(solution.insertIntoBST(root, val=25)))
