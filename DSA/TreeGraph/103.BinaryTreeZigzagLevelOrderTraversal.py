# Definition for a binary tree node.
from collections import deque
from typing import Optional, List


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def zigzagLevelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:

        def bfs(root: Optional[TreeNode]):
            if not root:
                return []

            turn = True
            queue = deque([root])
            res = []

            while queue:
                level = deque()

                for _ in range(len(queue)):
                    node = queue.popleft()

                    if turn:
                        level.append(node.val)
                    else:
                        level.appendleft(node.val)

                    if node.left:
                        queue.append(node.left)
                    if node.right:
                        queue.append(node.right)

                res.append(level)
                turn = not turn
            return res

        return bfs(root)


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

# values = [3, 9, 20, None, None, 15, 7]
# root = create_tree_from_list(values)
# print("Test case 1:", solution.zigzagLevelOrder(root))

values = [3, 9, 20, 8, None, None, 15, 7, 9, 2]
root = create_tree_from_list(values)
print("Test case 2:", solution.zigzagLevelOrder(root))
