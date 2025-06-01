# Definition for a binary tree node.
from collections import deque
from typing import Optional, List

class Solution:

    def inorderTraversal(root) -> List[int]:
        if root is None:
            return []
        
        left = Solution.inorderTraversal(root.left)
        right = Solution.inorderTraversal(root.right)

        return left + [root.val] + right

    def inorderTraversalStack2(root):
        res = []
        stack = []
        curr = root
        while stack or curr:
            while curr:
                stack.append(curr)
                curr = curr.left
            curr = stack.pop()
            res.append(curr.val)
            curr = curr.right

        return res
    
    def preorderTraversalStack(root):
        if not root:
            return []
        
        stack, result = [root], []
        
        while stack:
            node = stack.pop()
            result.append(node.val)
            
            if node.right:
                stack.append(node.right)
            if node.left:
                stack.append(node.left)
        
        return result



class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


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

values = [1,None,2,3]
root = create_tree_from_list(values)
print("Test case 1:", Solution.inorderTraversal(root)) #  [1, 3, 2]

values = [1,None,2,3]
root = create_tree_from_list(values)
print("Test case 1:", Solution.preorderTraversalStack(root)) #  [1, 3, 2]



values = [1,2,3,4,5,None,8,None,None,6,7,9]
root = create_tree_from_list(values)
print("Test case 2:", Solution.inorderTraversal(root)) # Output: [4,2,6,5,7,1,3,9,8]

values = [1,2,3,4,5,None,8,None,None,6,7,9]
root = create_tree_from_list(values)
print("Test case 2:", Solution.preorderTraversalStack(root)) # Output: [4,2,6,5,7,1,3,9,8]

# values = [1,2,3,4,5,None,8,None,None,6,7,9]
# root = create_tree_from_list(values)
# print("Test case 2:", Solution.postorderTraversalStack(root)) # Output: [4,2,6,5,7,1,3,9,8]