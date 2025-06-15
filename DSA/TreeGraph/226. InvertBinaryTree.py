# Definition for a binary tree node.
from collections import deque
from typing import Optional

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def invertTree(self, root: TreeNode) -> TreeNode: # DFS recursive approach 

        if not root:
            return None

        left = self.invertTree(root.left)
        right = self.invertTree(root.right)

        root.left = right
        root.right = left
        
        return root
    
    def invertTreeBFS(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        if not root:
            return None
        
        queue = deque([root]) # BFS approach
        while queue:
            curr = queue.popleft()

            curr.left, curr.right = curr.right, curr.left

            if curr.left:
                queue.append(curr.left)
            
            if curr.right:
                queue.append(curr.right)

        return root
    
    def invertTreeDFS(self, root: Optional[TreeNode]) -> Optional[TreeNode]: # DFS stack approach 
        if not root:
            return None

        stack = [root]
        while stack:
            curr = stack.pop()

            curr.left, curr.right = curr.right, curr.left

            if curr.left:
                stack.append(curr.left)
            if curr.right:
                stack.append(curr.right)

        return root



# Helper function to build a binary tree from a list
def build_tree(values):
    if not values:
        return None
    nodes = [TreeNode(val) if val is not None else None for val in values]
    kids = nodes[::-1]
    root = kids.pop()
    for node in nodes:
        if node:
            if kids: node.left = kids.pop()
            if kids: node.right = kids.pop()
    return root

# Helper function to convert a binary tree to a list (level-order traversal)
def tree_to_list(root):
    if not root:
        return []
    result, queue = [], [root]
    while queue:
        node = queue.pop(0)
        if node:
            result.append(node.val)
            queue.append(node.left)
            queue.append(node.right)
        else:
            result.append(None)
    while result and result[-1] is None:
        result.pop()
    return result

# Test cases
solution = Solution()

# Test case 1
tree1 = build_tree([4, 2, 7, 1, 3, 6, 9])
inverted1 = solution.invertTree(tree1)
print(f"Test case 1: {tree_to_list(inverted1)}")  # Expected: [4, 7, 2, 9, 6, 3, 1]

# Test case 2
tree2 = build_tree([2, 1, 3])
inverted2 = solution.invertTree(tree2)
print(f"Test case 2: {tree_to_list(inverted2)}")  # Expected: [2, 3, 1]

# Test case 3
tree3 = build_tree([1, None, 2, None, 3])
inverted3 = solution.invertTree(tree3)
print(f"Test case 3: {tree_to_list(inverted3)}")  # Expected: [1, 2, None, 3]