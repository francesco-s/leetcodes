# Definition for a Node.
from collections import defaultdict
from typing import Optional


class Node:
    def __init__(self, val=0, next=None, random=None):
        self.val = val
        self.next = next
        self.random = random

class Solution:

    # Time Complexity: O(N), where N is the number of nodes in the list.
    # Space Complexity: O(N), for the hashmap storing node copies.
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        if head is None:
            return None

        curr = head
        pairs = defaultdict(Node)

        while curr:
            new_node = Node(curr.val, None, None)
            pairs[curr] = new_node
            curr = curr.next

        new_head = pairs[head]
        curr = head

        while curr:
            pairs[curr].next = pairs[curr.next] if curr.next else None
            pairs[curr].random = pairs[curr.random] if curr.random else None
            curr = curr.next

        return new_head

# Helper function to create linked list from array of (val, random_index)
def create_random_list(arr):
    if not arr:
        return None

    nodes = [Node(val) for val, _ in arr]
    for i, (_, rand_idx) in enumerate(arr):
        if i < len(arr) - 1:
            nodes[i].next = nodes[i + 1]
        if rand_idx is not None:
            nodes[i].random = nodes[rand_idx]

    return nodes[0]

# Helper function to convert linked list to array of (val, random_index) for printing
def linked_list_to_array(head):
    if not head:
        return []
    
    result = []
    nodes = []
    node_map = {}
    current = head
    idx = 0
    
    # First pass: collect all nodes and map them to indices
    while current:
        nodes.append(current)
        node_map[current] = idx
        current = current.next
        idx += 1

    # Second pass: create result with (val, random_index)
    current = head
    while current:
        rand_idx = node_map[current.random] if current.random else None
        result.append((current.val, rand_idx))
        current = current.next

    return result

# Test cases
solution = Solution()

# Test case 1
arr1 = [(7, None), (13, 0), (11, 4), (10, 2), (1, 0)]
head1 = create_random_list(arr1)
result1 = solution.copyRandomList(head1)
print(f"Test case 1: {linked_list_to_array(result1)}")  # Expected: [(7, None), (13, 0), (11, 4), (10, 2), (1, 0)]

# Test case 2
arr2 = [(1, 1), (2, 1)]
head2 = create_random_list(arr2)
result2 = solution.copyRandomList(head2)
print(f"Test case 2: {linked_list_to_array(result2)}")  # Expected: [(1, 1), (2, 1)]

# Test case 3
arr3 = []
head3 = create_random_list(arr3)
result3 = solution.copyRandomList(head3)
print(f"Test case 3: {linked_list_to_array(result3)}")  # Expected: []

# Test case 4
arr4 = [(3, None)]
head4 = create_random_list(arr4)
result4 = solution.copyRandomList(head4)
print(f"Test case 4: {linked_list_to_array(result4)}")  # Expected: [(3, None)]

# Test case 5
arr5 = [(1, 2), (2, None), (3, 0)]
head5 = create_random_list(arr5)
result5 = solution.copyRandomList(head5)
print(f"Test case 5: {linked_list_to_array(result5)}")  # Expected: [(1, 2), (2, None), (3, 0)]
