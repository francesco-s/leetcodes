# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
from collections import deque


class Solution(object):
    def levelOrder(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: List[List[int]]
        """
        if not root:
            return []
        
        result = []

        def helper (node, level):
            if len(result) == level:
                result.append([])

            result[level].append(node.val)
            
            if node.left:
                helper(node.left, level + 1)
            if node.right:
                helper(node.right, level + 1)


        helper(root, 0)
        return result
        

# Helper function to construct a binary tree from a list
def build_tree(values):
    if not values:
        return None

    root = TreeNode(values[0])
    queue = deque([root])
    i = 1

    while queue and i < len(values):
        node = queue.popleft()
        if values[i] is not None:
            node.left = TreeNode(values[i])
            queue.append(node.left)
        i += 1

        if i < len(values) and values[i] is not None:
            node.right = TreeNode(values[i])
            queue.append(node.right)
        i += 1

    return root

# Test cases
root = build_tree([3, 9, 20, None, None, 15, 7])
print(Solution().levelOrder(root))  # Output: [[3], [9, 20], [15, 7]]

root = build_tree([1])
print(Solution().levelOrder(root))  # Output: [[1]]

root = build_tree([])
print(Solution().levelOrder(root))  # Output: []

 