# Definition for a binary tree node.
from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:

    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        """
        Inverts a binary tree by recursively swapping the left and right children of every node.
        Args:
            root (Optional[TreeNode]): The root node of the binary tree.
        Returns:
            Optional[TreeNode]: The root node of the inverted binary tree.
        Time Complexity (TC): O(n), where n is the number of nodes in the tree, since each node is visited once.
        Space Complexity (SC): O(h), where h is the height of the tree, due to the recursion stack.
        """
        if root is None:
            return

        left = self.invertTree(root.left)
        right = self.invertTree(root.right)

        root.left = right
        root.right = left

        return root

    def invertTreeUnpacking(self, root):
        if root is None:
            return None
        
        """
        # This doesn't work!
        if root is None:
            return

        root.left = self.invertTree(root.right)
        root.right = self.invertTree(root.left)

        return root
        """
        # Unpacking WORKS!
        root.left, root.right = self.invertTree(root.right), self.invertTree(root.left)

        return root

# Helper function to create binary tree from list (level-order traversal)
from collections import deque

def create_binary_tree(data):
    if not data:
        return None
    
    iter_data = iter(data)
    root = TreeNode(next(iter_data))
    queue = deque([root])
    
    while True:
        try:
            node = queue.popleft()
            left_val = next(iter_data)
            if left_val is not None:
                node.left = TreeNode(left_val)
                queue.append(node.left)
            right_val = next(iter_data)
            if right_val is not None:
                node.right = TreeNode(right_val)
                queue.append(node.right)
        except StopIteration:
            break
    return root

# Helper function to serialize tree to list (level-order) for printing
def tree_to_list(root):
    if root is None:
        return []
    
    result = []
    queue = deque([root])
    
    while queue:
        node = queue.popleft()
        if node:
            result.append(node.val)
            queue.append(node.left)
            queue.append(node.right)
        else:
            result.append(None)
    
    # Remove trailing None values
    while result and result[-1] is None:
        result.pop()
    return result

# Test cases
solution = Solution()

# Test case 1
root1 = create_binary_tree([4, 2, 7, 1, 3, 6, 9])
result1 = solution.invertTree(root1)
print(f"Test case 1: {tree_to_list(result1)}")  # Expected: [4, 7, 2, 9, 6, 3, 1]

# Test case 2
root2 = create_binary_tree([2, 1, 3])
result2 = solution.invertTree(root2)
print(f"Test case 2: {tree_to_list(result2)}")  # Expected: [2, 3, 1]

# Test case 3
root3 = create_binary_tree([])
result3 = solution.invertTree(root3)
print(f"Test case 3: {tree_to_list(result3)}")  # Expected: []

# Test case 4
root4 = create_binary_tree([1, None, 2])
result4 = solution.invertTree(root4)
print(f"Test case 4: {tree_to_list(result4)}")  # Expected: [1, 2]

# Test case 5
root5 = create_binary_tree([1, 2, None])
result5 = solution.invertTree(root5)
print(f"Test case 5: {tree_to_list(result5)}")  # Expected: [1, None, 2]

# Test case 6
root6 = create_binary_tree([1])
result6 = solution.invertTree(root6)
print(f"Test case 6: {tree_to_list(result6)}")  # Expected: [1]
